from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class ExternalUserController(http.Controller):

    @http.route('/external-users', auth='public', website=True)
    def show_external_users(self, **kwargs):
        users = request.env['external.user'].sudo().search([])
        return request.render('external_user_sync.external_user_page', {
            'users': users
        })

    @http.route('/sync-external-users', type='http', auth='user', methods=['POST'], csrf=True, website=True)
    def sync_users(self, **post):
        try:
            request.env['external.user'].sudo().sync_external_users()
            return request.redirect('/external-users')
        except Exception as e:
            _logger.exception("Failed to sync users")
            return request.render('external_user_sync.external_user_page', {
                'users': [],
                'error': str(e),
            })
