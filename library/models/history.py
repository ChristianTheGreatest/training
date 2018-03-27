# -*- coding: utf-8 -*-

from odoo import models, fields

class history(models.Model):
    _name = 'library.history'
    _description = 'Library History'
    name= fields.Char(string="Invoice ID")
    book_id = fields.Many2one(comodel_name="library.book", string="Book")
    customer_id = fields.Many2one(comodel_name="library.customer", string="Customer")
    checked_out = fields.Date(string="Checked Out Date")