# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class UserInformation(models.Model):
    _name = 'user.information'
    _description = 'User Information'

    name = fields.Char('Name', related='employee_id.name')
    employee_id = fields.Many2one('hr.employee', string="Employee")
    pc_name = fields.Many2one('account.asset', string='PC Name')
    pc_type = fields.Selection([('desktop','Desktop'),('laptop','Laptop')], string='PC Type')
    domain_user = fields.Char(string='Domain User')
    password = fields.Char(string='Password')
    vpn_user = fields.Char(string='VPN User')
    vpn_password = fields.Char(string='VPN Password')
    email = fields.Char(string='Email')
    email_password = fields.Char(string='Email Password')
    ip = fields.Char(string='IP')
    ext = fields.Char(string='EXT')
    new_local_user = fields.Char(string='New Local User')
    Local_user_password = fields.Char(string='Local User Password')


 




 