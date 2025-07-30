from odoo import models, fields, api
import secrets

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    api_key = fields.Char(string="API Key", copy=False)

    @api.model
    def create(self, vals):
        if not vals.get('api_key'):
            vals['api_key'] = secrets.token_hex(16)
        return super().create(vals)
