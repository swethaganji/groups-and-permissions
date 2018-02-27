# -*- coding: utf-8 -*-

from odoo import models, fields, api

class emp_permissions(models.Model):
    _name = 'emp_permissions.emp_permissions'

    
    name = fields.Char(string="Employee name")
    birthday = fields.Date('Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],string="Gender")
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string="Marital Status")
    
    mobile_phone = fields.Char(string="mobile number")
    work_email = fields.Char(string="Email")
    work_location = fields.Char(string="location")

class manager(models.Model):
	_name = 'emp_permissions.manager'
    


    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100