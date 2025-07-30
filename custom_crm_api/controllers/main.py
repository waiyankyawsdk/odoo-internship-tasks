from odoo import http
from odoo.http import request
import logging
import json

_logger = logging.getLogger(__name__)


class LeadFormPage(http.Controller):

    @http.route('/crm/form', type='http', auth='public', website=True)
    def lead_form_page(self, **kwargs):
        try:
            html = request.env['ir.ui.view']._render_template('custom_crm_api.lead_form_page', {})
            return request.make_response(html, headers=[('Content-Type', 'text/html')])
        except Exception:
            _logger.exception("Failed to render lead form template")
            return request.make_response(
                "<h1>500: Internal Server Error</h1><p>Could not load the lead form template.</p>",
                status=500,
                headers=[('Content-Type', 'text/html')]
            )


class LeadAPIController(http.Controller):

    @http.route('/api/create_lead', auth='public', methods=['POST'], csrf=False, type='http', cors=True)
    def create_lead(self):

        VALID_API_TOKEN = "2cfc121d1adb22d2e1a0aa29503d7bc28a07c600"

        auth_header = request.httprequest.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return http.Response(
                json.dumps({
                    'result': {
                        'success': False,
                        'error': 'Unauthorized: Missing or invalid Authorization header',
                        'code': 401
                    }
                }),
                status=401,
                content_type='application/json'
            )

        token = auth_header[7:].strip()
        if token != VALID_API_TOKEN:
            return http.Response(
                json.dumps({
                    'result': {
                        'success': False,
                        'error': 'Unauthorized: Invalid token',
                        'code': 401
                    }
                }),
                status=401,
                content_type='application/json'
            )


        try:
            data = request.httprequest.json  # cleaner than decode + loads
            _logger.debug("Received lead data: %s", data)
        except Exception:
            _logger.exception("Failed to parse JSON body")
            return http.Response(
                json.dumps({
                    'result': {
                        'success': False,
                        'error': 'Invalid JSON body',
                        'code': 400
                    }
                }),
                status=400,
                content_type='application/json'
            )

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        description = data.get('description')

        if not name or not email or not phone:
            return http.Response(
                json.dumps({
                    'result': {
                        'success': False,
                        'error': 'Missing required fields: name, email, and phone are mandatory',
                        'code': 400
                    }
                }),
                status=400,
                content_type='application/json'
            )

        try:
            lead = request.env['crm.lead'].sudo().create({
                'name': name,
                'email_from': email,
                'phone': phone,
                'description': description or ''
            })

            return http.Response(
                json.dumps({
                    'result': {
                        'success': True,
                        'message': 'Lead created successfully',
                        'lead': {
                            'id': lead.id,
                            'name': lead.name
                        }
                    }
                }),
                status=200,
                content_type='application/json'
            )

        except Exception as e:
            _logger.exception("Error while creating lead")
            return http.Response(
                json.dumps({
                    'result': {
                        'success': False,
                        'error': 'Internal Server Error: ' + str(e),
                        'code': 500
                    }
                }),
                status=500,
                content_type='application/json'
            )
