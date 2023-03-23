from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

from dateutil.relativedelta import relativedelta


class HotelTower(models.Model):
    _name = 'hotel.tower'
    _description = 'Details of Towers of hotels'

    name = fields.Char('Tower')
    state = fields.Selection([('under_construction', 'Under Construction'), ('ready_to_move_in', 'Ready to moveIn'), 
                            ('ready', 'Ready - working'), ('under maintance', 'Under maintance')])
    staff = fields.Char('Staff members')
    construction_agency_name = fields.Char('Construction Agency Name')
    establish_day = fields.Date('Establish Day')
    manager_name_id = fields.Many2one('hotel.staff.management', string='Manager name')
    cleaning_agency_name = fields.Char('Cleaning Agency')
    cleaning_agency_person = fields.Char('Cleaning Agency Person')
    # room_type_two = fields.Many2one('hotel.tower.rooms', string="Second Room type")
    tower_rooms_lines_ids = fields.One2many('hotel.tower.rooms.lines', 'tower_room_id', string="Rooms")
    representative = fields.Many2one('res.users', string="Representative")
    guest_count = fields.Integer('Guest count', compute="_compute_guest_count")

    def _compute_guest_count(self):
        self.guest_count = False
        # print('fadskfasjdfasdfasdjfsaddf\n\n', self.env.context)
        for rec in self:
            guests = self.env['hotel.guest'].search_count([
                ('tower_id', '=', rec.id)
            ])
            if guests:
                rec.guest_count = guests
            else:
                rec.guest_count = 0

    def action_count_guest_intower(self):
        vals = {
            'name': _('Guest'),
            'view_mode': 'tree,form',
            'domain': [('tower_id', '=', self.id)],
            'res_model': 'hotel.guest',
            'type': 'ir.actions.act_window',
            'context': {'is_guest' : True},
        }
        return vals

class HotelTowerRooms(models.Model):
    _name = 'hotel.tower.rooms.lines'
    _description = 'Details of rooms in tower'
    _rec_name = 'room'


    room = fields.Char('Room type')
    room_type = fields.Selection([('ac', 'AC'), ('non_ac', 'Non AC')], string='Types of Rooms')
    nos_room = fields.Integer('Nos of rooms')
    available_rooms = fields.Integer('Available rooms', compute="_compute_nos_rooms")
    tower_room_id = fields.Many2one('hotel.tower', string="Tower")
    is_available_room = fields.Boolean('Is available room', default=True)
    room_price = fields.Integer('Room unit price')
    guest_id = fields.Many2one('hotel.guest', string="Guest Name")
    # selected_check_in = fields.Datetime(related='guest_id.check_in_time')
    # selected_check_out = fields.Datetime(related='guest_id.check_out_time')


    @api.constrains('room', 'room_type', 'tower_room_id')
    def check_duplicate_name(self):
        for rec in self:
            my_duplicate_result = self.env['hotel.tower.rooms.lines'].search([('room', '=', rec.room), 
                ('room_type', '=', rec.room_type), ('tower_room_id', '=', rec.tower_room_id.id)])
            if len(my_duplicate_result) > 1:
                raise ValidationError('Category of two room can not be same')

    # @api.depends('room')
    def _compute_nos_rooms(self):
        self.available_rooms = False
        for rec in self:
            av_room = rec.nos_room
            my_result = self.env['hotel.guest'].search([('tower_id', '=', rec.tower_room_id.id),
                    ('room_id', '=', rec.room), ('room_type', '=', rec.room_type)])
            if my_result:
                av_room = av_room - len(my_result)
            if av_room==0:
                rec.is_available_room = False
            else:
                rec.is_available_room = True
            rec.available_rooms = av_room

    def name_get(self):
        result = []
        for rec in self:
            if self.env.context.get('custom_search', False):
                result.append((rec.id, rec.room))
            else:
                result.append((rec.id, f"{rec.room} - {rec.room_type} - ({rec.room_price})"))
        return result
