from odoo import models, fields
import requests


class ExternalUser(models.Model):
    _name = 'external.user'
    _description = 'External User'

    name = fields.Char(required=True)
    email = fields.Char()
    street = fields.Char()
    city = fields.Char()

    def sync_external_users(self):
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        if response.status_code == 200:
            users = response.json()
            for user in users:
                existing = self.env['external.user'].search([('email', '=', user['email'])], limit=1)
                if not existing:
                    self.env['external.user'].create({
                        'name': user['name'],
                        'email': user['email'],
                        'street': user['address']['street'],
                        'city': user['address']['city'],
                    })
        else:
            raise Exception(f"Failed to fetch users: {response.status_code}")
