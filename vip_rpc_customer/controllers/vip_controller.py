from odoo import http
from odoo.http import request

class VipCustomerController(http.Controller):
    @http.route('/vip-customers', type='http', auth='public', website=True)
    def vip_customer_page(self, **kw):
        partners = request.env['res.partner'].sudo().search([], limit=100)
        return request.render('vip_rpc_customer.vip_customer_template', {'partners': partners})
