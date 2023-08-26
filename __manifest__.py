{
    'name': 'Immobilier',
    'version': '1.0',
    'description': '',
    'summary': 'Module de gestion immobilière',
    'author': 'Djogona Mahamat',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Immobilier',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menus_views.xml',
        'views/estate_property_views.xml',
    ],
    'auto_install': False,
    'application': True,
}