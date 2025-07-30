from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class CustomerAPI(http.Controller):

    @http.route('/api/customers', type='json', auth="none", methods=['POST'], csrf=False)
    def fetch_customers(self, **kwargs):

        token = request.httprequest.headers.get('Authorization')

        if not token:
            _logger.warning("Missing API token")
            return {'error': 'Missing API token'}

        valid_token = request.env['customer.api.key'].sudo().search([
            ('name', '=', token),
            ('active', '=', True)
        ], limit=1)

        if not valid_token:
            _logger.warning("Invalid API token: %s", token)
            return {'error': 'Invalid API token'}

        domain = ['|', ('customer', '=', True), ('customer_rank', '>', 0)]

        customers = request.env['res.partner'].sudo().search(domain)

        customer_data = [{
            'id': customer.id,
            'name': customer.name or '',
            'email': customer.email or '',
            'phone': customer.phone or '',
            'image': f"/web/image/res.partner/{customer.id}/image_1920"
        } for customer in customers]

        _logger.info("API fetched %d customers", len(customer_data))

        return {'customers': customer_data}

    @http.route('/web/customers', type='http', auth="public", website=True)
    def web_customer_list(self, **kwargs):

        domain = [('active', '=', True)]

        customers = request.env['res.partner'].sudo().search(domain)

        customer_count = request.env['res.partner'].sudo().search_count(domain)
        _logger.info("Website page loaded with %d customers", customer_count)

        return request.render('customer_list_api.customer_view_template', {
            'customers': customers
        })
