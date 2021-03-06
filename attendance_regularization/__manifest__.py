{
    'name': "Open HRMS Attendance Regularization",
    'version': '12.0.1.0.0',
    'summary': """Assigning Attendance for the Employees with Onsight Jobs""",
    'description': """Assigning Attendance for the Employees with Onsight Jobs through the requests by Employees """,
    'category': 'Human Resources',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.openhrms.com",
    'depends': ['base', 'hr','hr_attendance','project','contacts','oh_employee_creation_from_user'],
    'data': [
            'security/ir.model.access.csv',
             'security/security.xml',
             'views/category.xml',
             'views/regularization_views.xml',
            ],
    'demo': [],
    'images': ['static/description/banner.jpg'],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
