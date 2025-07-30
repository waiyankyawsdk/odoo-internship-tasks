{
    'name': 'Customer API',
    'version': '1.0',
    'summary': 'Expose API to create CRM leads with token authentication',
    'category': 'Sales',
    'author': 'Thinzar Htun',
    'depends': ['base', 'crm', 'website'],
    'data': [
        'views/customer_template.xml',
        'views/customer_menu.xml',
    ],
    'installable': True,
    'application': False,
}
