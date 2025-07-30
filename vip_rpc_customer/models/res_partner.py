from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_vip = fields.Boolean(string="VIP Customer", default=False)

    @api.model
    def mark_as_vip(self, partner_ids):
        partners = self.browse(partner_ids)
        vip_category = self.env['res.partner.category'].search([('name', '=', 'VIP')], limit=1)
        if not vip_category:
            vip_category = self.env['res.partner.category'].create({'name': 'VIP'})

        for partner in partners:
            partner.is_vip = True
            if vip_category.id not in partner.category_id.ids:
                partner.category_id = [(4, vip_category.id)]
        return True
