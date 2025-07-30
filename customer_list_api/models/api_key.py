from odoo import models, fields
import secrets

class CustomerAPIKey(models.Model):
    _name = 'customer.api.key'
    _description = 'API Key for Customer Access'

    name = fields.Char(string="API Key", required=True, readonly=True, default=lambda self: secrets.token_urlsafe(32))
    active = fields.Boolean(default=True)
    description = fields.Text()
