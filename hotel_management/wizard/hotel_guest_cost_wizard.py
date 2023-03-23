from odoo import fields, models, api, _


class HotelGuestCost(models.TransientModel):
    _name = 'hotel.guest.cost.wizard'
    _description = 'Tentative amount of guest during stay in hotel'

    guest_id = fields.Many2one('hotel.guest', 'Name')
    check_in_time = fields.Date(related="guest_id.check_in_time", string='Check In')
    check_out_time = fields.Date(related="guest_id.check_out_time", string='Check Out')
    no_of_days = fields.Integer(related="guest_id.no_of_days", string='Days in Hotel')
    final_total = fields.Integer(related="guest_id.final_total", string='Total')
    state = fields.Selection(related="guest_id.state", string="State", readonly=False)

    @api.model
    def default_get(self, fields):
        res = super(HotelGuestCost, self).default_get(fields)
        res_ids = self._context.get('active_ids')

        guest = self.env['hotel.guest'].browse(res_ids)
        # self.guest_id = guest
        res['guest_id'] = guest
        return res

    def confirm_check_in(self):
        self.guest_id.state = 'confirm'
        # print('confirm is working')