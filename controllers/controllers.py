# -*- coding: utf-8 -*-
# from odoo import http


# class ShfTecnicTest(http.Controller):
#     @http.route('/shf_tecnic_test/shf_tecnic_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shf_tecnic_test/shf_tecnic_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shf_tecnic_test.listing', {
#             'root': '/shf_tecnic_test/shf_tecnic_test',
#             'objects': http.request.env['shf_tecnic_test.shf_tecnic_test'].search([]),
#         })

#     @http.route('/shf_tecnic_test/shf_tecnic_test/objects/<model("shf_tecnic_test.shf_tecnic_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shf_tecnic_test.object', {
#             'object': obj
#         })
