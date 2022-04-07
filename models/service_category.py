# -*- coding: utf-8 -*-

# import de odoo
from odoo import models, fields, api, _


class ServiceCategory(models.Model):
    _name = 'shf.service.category'
    _description = 'Model for service guide records'

    # fields
    name = fields.Char(
        string='Name',
        required=True
    )

    # constraint
    @api.constrains('name')
    def constrain_unique_name(self):
        if self.search([('name', '=', self.name.lower()), ('id', '!=', self.id)]):
            raise Warning(_('Las categorias deben ser unicas!'))

