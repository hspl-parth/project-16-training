from odoo import models, fields, api


class HotelGuestDocuments(models.Model):
    _name = 'guest.documents'
    _description = 'Details Documents and documents types'

    name = fields.Char('Document name')
    is_required = fields.Boolean('Required')
    