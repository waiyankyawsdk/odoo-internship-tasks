{
    'name': 'External User Sync',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Import external users and show on website',
    'depends': ['base', 'website'],
    'data': [
        'views/external_user_views.xml',
        'views/external_user_template.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
