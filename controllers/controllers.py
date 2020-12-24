# -*- coding: utf-8 -*-
from odoo import http

# class MethodInvoiceTermal(http.Controller):
#     @http.route('/method_invoice_termal/method_invoice_termal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_invoice_termal/method_invoice_termal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_invoice_termal.listing', {
#             'root': '/method_invoice_termal/method_invoice_termal',
#             'objects': http.request.env['method_invoice_termal.method_invoice_termal'].search([]),
#         })

#     @http.route('/method_invoice_termal/method_invoice_termal/objects/<model("method_invoice_termal.method_invoice_termal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_invoice_termal.object', {
#             'object': obj
#         })