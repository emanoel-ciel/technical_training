
{
    'name': 'Estate',
    'version': '1.0',
    'license':'LGPL-3',
    'depends': ['base'],
    'application': True,
    'author': 'Emanoel Fuentes',
    'data': [
        # Data
        'data/res_groups.xml',
        'data/demo.xml',

        # Security
        'security/ir.model.access.csv',

        # Views
        'views/estate_actions.xml',
        'views/estate_menu.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
    ]
}