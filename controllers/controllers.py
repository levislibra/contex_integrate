# -*- coding: utf-8 -*-
from openerp import http

# class ContexIntegrate(http.Controller):
#     @http.route('/contex_integrate/contex_integrate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contex_integrate/contex_integrate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contex_integrate.listing', {
#             'root': '/contex_integrate/contex_integrate',
#             'objects': http.request.env['contex_integrate.contex_integrate'].search([]),
#         })

#     @http.route('/contex_integrate/contex_integrate/objects/<model("contex_integrate.contex_integrate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contex_integrate.object', {
#             'object': obj
#         })