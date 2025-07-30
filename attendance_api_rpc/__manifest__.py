{
    'name': 'Attendance JSON-RPC API',
    'version': '1.0',
    'summary': 'API to get today attendance via JSON-RPC',
    'category': 'Human Resources',
    'author': 'Thinzar Htun',
    'depends': ['hr_attendance', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/attendance_template.xml',
    ],
    'installable': True,
    'application': False,
}
