# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ServiceGuideLine(models.Model):
    _name = 'shf.service.guide.line'
    _description = 'Model for service guide line records'

    # defaults y compute
    @api.onchange('amount', 'discount')
    def onchange_set_zero(self):
        if self.amount < 0:
            self.amount = 0            
        if self.discount < 0:
            self.discount = 0

    @api.depends('amount', 'discount')
    def compute_total_amount(self):
        for line in self:            
            total = line.amount
            if line.discount:
                total = (1 - (line.discount / 100)) * line.amount
            line.total_amount = total

    # fields
    name = fields.Char(
        string='name',
        required=True,
    )

    amount = fields.Float(
        string='Amount',
        digits=(12, 2),
        required=True,
    )

    discount = fields.Integer(
        string='Discount %',
        default=0,
        required=True,
    )

    total_amount = fields.Float(
        string='Total',
        compute=compute_total_amount,
        readonly=True,
    )

    service_guide_id = fields.Many2one(
        'shf.service.guide',
        string='Service Guide',
        required=True,
    )
