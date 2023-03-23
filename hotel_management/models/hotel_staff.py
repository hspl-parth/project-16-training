from odoo import models, fields, api


class HotelStaffCleaning(models.Model):
    _name = 'hotel.staff.cleaning'
    _description = 'Details of Cleaning staff of hotel'

    name = fields.Char('Name', help="Name of Cleaning person")
    dob = fields.Date('Date of birth')
    age = fields.Integer('Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    photo = fields.Binary('Photo')
    email = fields.Char('Email')
    contact_number = fields.Char('Phone')
    address = fields.Text('Address')



class HotelStaffManagement(models.Model):
    _name = 'hotel.staff.management'
    _description = 'Details of Management staff of hotel'

    name = fields.Char('Name')
    dob = fields.Date('Date of birth')
    age = fields.Integer('Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    photo = fields.Binary('Photo')
    email = fields.Char('Email')
    contact_number = fields.Char('Phone')
    address = fields.Text('Address')



class HotelStaffWaiter(models.Model):
    _name = 'hotel.staff.waiter'
    _description = 'Details of Waiter staff of hotel'

    name = fields.Char('Name')
    dob = fields.Date('Date of birth')
    age = fields.Integer('Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    photo = fields.Binary('Photo')
    email = fields.Char('Email')
    contact_number = fields.Char('Phone')
    address = fields.Text('Address')



class HotelStaffSecurity(models.Model):
    _name = 'hotel.staff.security'
    _description = 'Details of Security staff of hotel'

    name = fields.Char('Name')
    dob = fields.Date('Date of birth')
    age = fields.Integer('Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    photo = fields.Binary('Photo')
    email = fields.Char('Email')
    contact_number = fields.Char('Phone')
    address = fields.Text('Address')