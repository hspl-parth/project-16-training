from odoo import models, fields, api


class HotelGuestDocumentsLines(models.Model):
    _name = 'guest.documents.lines'
    _description = 'Details of guest documents'

    guest_id = fields.Many2one('hotel.guest','Guest name')
    dob = fields.Date(related="guest_id.dob", string='Date of birth')
    age = fields.Char(related="guest_id.age", string='Age')
    gender = fields.Selection(related="guest_id.gender", string='Gender')
    file = fields.Binary('Uplod file')
    document_name_id = fields.Many2one('guest.documents','Document name')
    # submited_ids = fields.Many2many('guest.documents', 'submited_ids_rel', 'name', 'guest_id', string="Submited ids")