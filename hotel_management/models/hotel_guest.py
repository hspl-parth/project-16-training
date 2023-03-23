from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

from dateutil.relativedelta import relativedelta
from datetime import date, datetime


class HotelGuest(models.Model):
    _name = 'hotel.guest'
    _description = 'Hotel Guest records and details'
    _rec_names_search = ['name', 'dob', 'gender', 'email']
    
    name = fields.Char('Guest name', required='1')
    reference = fields.Char(string="Reference", copy=False, readonly=True, default=lambda self: _('New'))
    dob = fields.Date('Date of birth')
    age = fields.Char('Age', compute="_compute_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    photo = fields.Binary('Photo')
    email = fields.Char('Email')
    contact_number = fields.Char('Phone')
    address = fields.Text('Address')
    state = fields.Selection([('check_in', 'Check In'), ('confirm', 'Confirm'), ('check_out', 'Check Out')], string="State")
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    city = fields.Char('cityity')
    state_id = fields.Char('State_id')
    zipcode = fields.Char('zipcode')
    country_id = fields.Char('Country')
    note = fields.Text('Notes')
    tower_id = fields.Many2one('hotel.tower', string="Tower")
    room_id = fields.Many2one('hotel.tower.rooms.lines', string="Room")
    room_type = fields.Selection(related="room_id.room_type", string='Types of Rooms')
    guest_documents_ids = fields.One2many('guest.documents.lines', 'guest_id', string="Documents")
    submited_ids = fields.Many2many('guest.documents', string="Submited ids")
    sub_total = fields.Integer('Sub Total', compute="_compute_sub_total")
    check_in_time = fields.Date('Check In')
    check_out_time = fields.Date('Check Out')
    no_of_days = fields.Integer('Days in hotel', compute="_compute_stay_in_hotel")
    taxes = fields.Integer('Taxes', compute="_compute_taxes")
    final_total = fields.Integer('Total', compute="_compute_total_amount")
    room_price = fields.Integer(related="room_id.room_price", string="Room Price")

    cal_room_price = fields.Integer('Hotel Stay cost', compute="_compute_room_price")

    @api.model_create_multi
    def create(self, vals):
        # print('\n\n', vals)
        for rec in vals:
            if not rec.get('reference') or rec['reference'] == _('New'):
                rec['reference'] = self.env['ir.sequence'].next_by_code('hotel.guest.seq') or _('New')
        res = super().create(vals)
        return res

    @api.depends('dob')
    def _compute_age(self):
        # print('hotel guest is here \n\n', self.env.context)
        self.age = False
        for rec in self:
            today = date.today()
            guest_dob = rec.dob
            result = relativedelta(today, guest_dob)
            rec.age = f"{result.years} years {result.months} months {result.days} days"

    @api.constrains('dob')
    def ckeck_birth_day(self):
        for rec in self:
            today = date.today()
            guest_dob = rec.dob
            result = relativedelta(today, guest_dob)
            if int(result.years) <= 10:
                raise ValidationError('Sorry, we can not give stay anyone below 10 years old')

    @api.constrains('tower_id', 'room_id')
    def check_available_rooms(self):
        for rec in self:
            available_rooms_id = self.env['hotel.tower.rooms.lines'].browse(rec.room_id.id)
            avl_room = available_rooms_id.available_rooms
            # print('\n\n', avl_room)

    @api.onchange('tower_id')
    def _onchange_tower_id(self):
        for rec in self:
            return {'domain': {'room_id': [('tower_room_id', '=', rec.tower_id.id), ('is_available_room', '=', True)]}}

    def _compute_stay_in_hotel(self):
        self.no_of_days = False
        for rec in self:
            check_in = rec.check_in_time
            check_out = rec.check_out_time
            result = relativedelta(check_out, check_in)
            rec.no_of_days = result.days

    def _compute_room_price(self):
        self.cal_room_price = False
        for rec in self:
            guest_time = rec.no_of_days
            rec.cal_room_price = guest_time * rec.room_id.room_price
            # rec.cal_room_price = 10

    def _compute_sub_total(self):
        self.sub_total = False
        for rec in self:
            rec.sub_total = rec.cal_room_price

    def _compute_taxes(self):
        self.taxes = False
        for rec in self:
            rec.taxes = (rec.sub_total*18/100)

    def _compute_total_amount(self):
        self.final_total = False
        for rec in self:
            rec.final_total = rec.sub_total + rec.taxes

    # def confirm_check_in(self):
    #     self.state = 'confirm'

    def check_out(self):
        self.state = 'check_out'

    def cron_happy_birthday(self):
        template_mail = self.env.ref('hotel_management.mail_template_hotel_management')
        # print('\n\n', dir(self._context))
        # filter_mails = self.env['hotel.guest'].search([]).mapped('dob')
        today = date.today()
        # result = relativedelta(today, rec)
        filter_mails = self.search([]).filtered(lambda l: l.dob and relativedelta(today, l.dob).months == 0 and relativedelta(today, l.dob).days == 0)
        # print('\n\n', filter_mails)
        for rec in filter_mails:
            # print('\n\n', rec)
            # today = date.today()
            # result = relativedelta(today, rec)
            # if result.months == 0 and result.days == 0:
            #     res = self.env['hotel.guest'].search([('dob', '=', rec)])
            template_mail.send_mail(rec.id)


