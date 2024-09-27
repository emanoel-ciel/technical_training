
{
    'name': 'Estate',
    'version': '1.0',
    'license':'LGPL-3',
    'depends': ['base'],
    'application': True,
    'author': 'Emanoel Fuentes',
    'data': [
        # Security
        'security/ir.model.access.csv',
        'security/res_groups.xml',

        # Data
        'data/demo.xml',

        # Views
        'views/estate_property_views.xml',
    ]
}