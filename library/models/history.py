# -*- coding: utf-8 -*-

from odoo import models, fields, api

class history(models.Model):
    _name = 'library.history'
    _description = 'Library History'
    name= fields.Char(string="Invoice ID")
    book_id = fields.Many2one(comodel_name="library.book", string="Book")
    customer_id = fields.Many2one(comodel_name="library.customer", string="Customer")
    checked_out = fields.Date(string="Checked Out Date")
    returned = fields.Boolean(compute="_check_returned",store = True, string="Is Returned")

    @api.multi
    @api.depends("checked_out")
    def _check_returned(self):
        for record in self:
            if record.checked_out is  not False:
                returned = True
            else:
                returned = False