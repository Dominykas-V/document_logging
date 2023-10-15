# -*- coding: utf-8 -*-
# from odoo import http


# class DocumentLogging(http.Controller):
#     @http.route('/document_logging/document_logging', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/document_logging/document_logging/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('document_logging.listing', {
#             'root': '/document_logging/document_logging',
#             'objects': http.request.env['document_logging.document_logging'].search([]),
#         })

#     @http.route('/document_logging/document_logging/objects/<model("document_logging.document_logging"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('document_logging.object', {
#             'object': obj
#         })
