{
    'name': 'College Management',
    'version': '1.1',
    'author':'Whiz IT solutions',
    'category': 'College Management',
    'description': """
        Module for College management.
            """,
    'depends': ['base'],
    'data': [
        'data/stud_data.xml',
        'views/stud_view.xml',
        'views/cl_view.xml',
        'views/res_partner_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable':True,
}
