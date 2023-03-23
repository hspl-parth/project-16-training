from odoo import models, fields, api

class HotelInhetirEmployee(models.Model):
    _inherit = "hr.employee"
    _description = 'Adding some fields to upload data from csv file'

    external_id = fields.Char('External ID')
    our_id = fields.Char(string="ID")
    # job_title = fields.Char('Job Title')
    division = fields.Char('Division')
    staff_category = fields.Char('Staff Category')
    location = fields.Char('Location')