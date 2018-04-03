# -*- coding: utf-8 -*-

from odoo import models, fields, api

class book(models.Model):
    _name = 'library.book'
    _description = 'Library book'
    name = fields.Char(string='Title',help='Enter the name of the book.', required=True, copy=False)
    publisher = fields.Char(string='Publisher')
    author_ids = fields.Many2many(comodel_name="library.author", string="Authors")
    cover = fields.Binary(string="Image")
    copies = fields.Integer(string='Number of Copies', required=True, default=1)
    published_date = fields.Date(string='Date Published')
    history_ids = fields.One2many(comodel_name="library.history", inverse_name="book_id", string='History')
    minimum_quantity = fields.Integer(string="Minimum Quantity", default=1)
    needs_reorder = fields.Boolean(compute="_check_book_reorder", string="Needs Reorder")


    @api.multi
    @api.depends("copies", "minimum_quantity")
    def _check_book_reorder(self):
        for record in self:
            if record.copies <= record.minimum_quantity:
                record.needs_reorder = True
                print(record.copies)
            else:
                record.needs_reorder = False

    



    
