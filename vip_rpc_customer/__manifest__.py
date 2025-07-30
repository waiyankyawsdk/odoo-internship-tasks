{
    'name': "VIP RPC Customer",
    'version': '1.0',
    'category': 'Website',
    'summary': 'Mark customers as VIP using RPC',
    'depends': ['base', 'web', 'website'],
    'data': [
        'views/res_partner_views.xml',
        'views/website_vip_customers.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'vip_rpc_customer/static/src/js/vip_button.js',
        ],
    },
    'installable': True,
    'application': False,
}
