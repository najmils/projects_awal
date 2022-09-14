# -*- coding: utf-8 -*-
# from odoo import http


# class Rukosme(http.Controller):
#     @http.route('/rukosme/rukosme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rukosme/rukosme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rukosme.listing', {
#             'root': '/rukosme/rukosme',
#             'objects': http.request.env['rukosme.rukosme'].search([]),
#         })

#     @http.route('/rukosme/rukosme/objects/<model("rukosme.rukosme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rukosme.object', {
#             'object': obj
#         })
