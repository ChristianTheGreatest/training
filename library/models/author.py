# -*- coding: utf-8 -*-

from odoo import models, fields

class author(models.Model):
    _name = 'library.author'
    _description = 'Library author'
    name = fields.Char(string='Name',help='Enter the name of the author.', required=True, copy=False)
    bio = fields.Char(string="Bio")
    books_id = fields.Many2many("library.book", string="Books")
    
    