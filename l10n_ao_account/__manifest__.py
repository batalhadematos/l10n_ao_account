# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Angola - Accounting',
    'countries': ['ao'],
    'version': '1.0.0',
    'author': 'Paulo Matos',
    'website': 'https://github.com/batalhadematos',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the module to manage the accounting chart for Angola in Odoo 19.
========================================================================

""",
    'images': ['static/description/module_image.png'],
    'depends': [
        'account',
    ],
    
    'data': [
        'data/res_country_data.xml',
        'views/account_account_view.xml',
    ],
    
    'demo': [],
    
    'auto_install': ['account'],
    'module_type': 'official',
    'license': 'LGPL-3',
}
