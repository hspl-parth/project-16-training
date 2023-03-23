{
    'name': 'User Information',
    'version': '16.0.1.0.1',
    'license': 'LGPL-3',
    'description': """ 
    user information.
    """,
    'sequence': 0,
    'depends': ['helpdesk' ,'account_asset'],
    'summary': "user information",
    'author': "entrivis",
    'category': 'Human Resources',
    'data': [
        'security/ir.model.access.csv',
        'views/user_information_views.xml',

            ],
    'demo': [
        ''
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}