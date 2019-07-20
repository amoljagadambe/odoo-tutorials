# -*- coding: utf-8 -*-
{
    'name': 'School Management',
    'version': '1.1',
    'author':'Whiz IT solutions',
    'category': 'School Management',
    'description': """
        Module for School management.
            """,
    'depends': ['base','website'],
    'data': [
        'views/student_view.xml',
        'security/ir.model.access.csv',
        'views/class_view.xml',
        'data/student_data.xml',
        'views/res_partner_view.xml',
        'views/template.xml'
    ],
    'installable':True,
}
