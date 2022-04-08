# -*- coding:utf-8 -*-
# importados de python

# importados de odoo
from odoo import http
from odoo.http import request

class RetentionController(http.Controller):

    @http.route('/service_guide', methods=['GET'], csrf=False, auth='user', website=True)
    def list_view(self):
        return request.render("shf_tecnic_test.service_guide", {
            'records': request.env['shf.service.guide'].search([], order='id desc')
        })

    @http.route('/service_guides/<model("shf.service.guide"):record>', methods=['GET'], csrf=False, auth='user', website=True)
    def form_view(self, record):
        return request.render("shf_tecnic_test.service_guide_form", {'record': record})
