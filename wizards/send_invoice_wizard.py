# -*- coding: utf-8 -*-
import base64, logging
# import de odoo
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)

class SendInvoiceWizard(models.TransientModel):
    _name = 'shf.send.invoice.wizard'
    _description = 'Model for service guide records'

    @api.model
    def create(self, values):
        # enviar email
        template = self.sudo().env.ref('shf_tecnic_test.shf_service_guide_details_mail')
        domain = [('model', '=', 'shf.service.guide'), ('report_name', '=', 'shf_tecnic_test.shf_service_guide_detail_report')]
        report = self.sudo().env['ir.actions.report'].search(domain, limit=1)
        guide = self.env['shf.service.guide'].browse(self._context.get('active_id'))

        if template:
            try:
                pdf = report._render_qweb_pdf([guide.id], {})[0]
                attachment = self.env['ir.attachment'].create({
                    'name': guide.name,
                    'store_fname': guide.name,
                    'datas': base64.b64encode(pdf)
                })
                template.with_context(data={'attachment_ids': [attachment]}).send_mail(guide.id)
            except Exception as error:
                _logger.info(error)

        return super(SendInvoiceWizard, self).create(values)

    # fields
    service_guide_id = fields.Many2one(
        'shf.service.guide',
        default=lambda self: self._context.get('active_id'),
    )

    email = fields.Char(
        related='service_guide_id.contact_id.email',
        store=True,
    )

    aditional_info = fields.Text(
        string='Aditional info'
    )
