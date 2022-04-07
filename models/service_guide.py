# -*- coding: utf-8 -*-
from datetime import date

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class ServiceGuide(models.Model):
    _name = 'shf.service.guide'
    _description = 'Model for service guide records'

    # CRUD
    @api.model
    def create(self, values):
        values.update({
            'name': self.env['ir.sequence'].next_by_code('shf.service.guide')
        })
        return super(ServiceGuide, self).create(values)

    # actions
    def action_draft(self):
        return self._set_state('draft')

    def action_approved(self):
        if not self.line_ids:
            raise Warning(_('Need add one or more lines to invoice.'))
        return self._set_state('approved')

    def action_completed(self):
        return self._set_state('completed')
    
    def action_canceled(self):
        return self._set_state('canceled')
    
    def action_finished(self):
        return self._set_state('finished')

    def _set_state(self, state):
        if state == self.state:
            return False
        if state in ('completed', 'finished', 'cancel'):
            if not self.env.user.has_group('shf_tecnic_test.shf_group_approvator'):
                raise Warning(_('Only the approvator role user qualify to change this states.'))
        return self.write({'state': state})

    # default
    @api.depends('line_ids')
    def compute_total_amount(self):
        total = 0
        for line in self.line_ids:
            total += line.total_amount
        self.amount = total

    # fields
    name = fields.Char(
        string='Code',
        readonly=True,
        store=True,
        default='--',
        required=True,
        help='Code sequence'
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
        ('finished', 'Finished')
    ],  string='State',
        default='draft',
        help='State of the service',
    )

    contact_id = fields.Many2one(
        'res.partner',
        string='Contact',
        required=True,
        help='Contact information',
    )

    category_id = fields.Many2one(
        'shf.service.category',
        string='Category',
        required=True,
        help='Category of service',
    )

    observations = fields.Text(
        string='Observations',
        help='Details of the service'
    )

    line_ids = fields.One2many(
        comodel_name='shf.service.guide.line',
        inverse_name='service_guide_id',
        string='Lines',
    )

    amount = fields.Float(
        string='Amount',
        compute=compute_total_amount,
        store=True,
    )

    date_guide = fields.Date(
        string='Date',
        default=date.today(),
        required=True,
        help='This is taked into the graphs',
    )
