# -*- coding: utf-8 -*-

from odoo import models, fields

class customer(models.Model):
    _name = 'library.customer'
    _description = 'Library Patron'
    name= fields.Char(string="Patron Name")
    age = fields.Integer(string="Age")
    history_id = fields.One2many("library.history", "customer_id", string="History")