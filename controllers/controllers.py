# -*- coding: utf-8 -*-
from odoo import http

# class S3-storage(http.Controller):
#     @http.route('/s3-storage/s3-storage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s3-storage/s3-storage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('s3-storage.listing', {
#             'root': '/s3-storage/s3-storage',
#             'objects': http.request.env['s3-storage.s3-storage'].search([]),
#         })

#     @http.route('/s3-storage/s3-storage/objects/<model("s3-storage.s3-storage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s3-storage.object', {
#             'object': obj
#         })