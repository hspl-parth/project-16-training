{
    'name': 'Hotel Management',
    'version': '16.0.1.0.0',
    'license': 'LGPL-3',
    'description': """ 
    Hotel management system for full flage soultion control.
    """,
    'sequence': 0,
    'depends': ['base', 'mail', 'website', 'report_xlsx', 'hr'],
    'summary': "Hotel Management",
    'author': "Heliconia",
    'category': 'Management',
    'data': [
            'security/ir.model.access.csv',
            'security/security.xml',
            'data/data.xml',
            'data/mail_template_data.xml',
            'data/hotel_guest_dob_cron.xml',
            'wizard/hotel_guest_cost_wizard_view.xml',
            'views/hotel_guest_view.xml',
            'views/hotel_tower_view.xml',
            'views/hotel_staff_cleaning_view.xml',
            'views/hotel_staff_management_view.xml',
            'views/hotel_staff_security_view.xml',
            'views/hotel_staff_waiter_view.xml',
            'views/hotel_guest_documents.xml',
            'views/hotel_tower_rooms_view.xml',
            'views/hotel_website_home.xml',
            'views/hotel_website_form.xml',
            'views/hotel_inherit_employee_view.xml',
            'views/menuitems.xml',
            'report/hotel_guest_detail_template.xml',
            'report/report.xml'
    ],
    'demo': [
        ''
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}