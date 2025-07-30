{
    'name': 'Custom CRM API',
    'version': '1.0',
    'summary': 'Expose API to create CRM leads with token authentication',
    'category': 'Sales',
    'author': 'Thinzar Htun',
    'depends': ['crm', 'website'],
    'data': [
        'views/lead_form_website_menu.xml',
        'views/lead_form_template.xml',
    ],
    'installable': True,
    'application': True,
}
