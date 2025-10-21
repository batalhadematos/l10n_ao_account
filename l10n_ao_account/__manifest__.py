# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2019 Paulo Matos. All Rights Reserved
# Paulo Matos - batalhadematos@gmail.com

{
    'name': 'Angola - Accounting',
    'version': '1.0.0',
    'author': 'Paulo Matos',
    'website': 'https://github.com/batalhadematos',
    'category': 'Localization',
    'description': """
    
Angola Basic Chart of Accounts (PGCA)
======================================

Angolan basic charts for accounting and basic localization data.

Includes:
    - Move accounts;
    - Provinces;
    - Banks;
    - Basic Tax setup (IVA);
    
Install Instructions:
- Refer to notes
    
    """,
    'depends': ['base', 'account'],
    'images': ['static/description/module_image.png'],            
    
    'data': [
           'data/l10n_ao_chart_data.xml',
           'data/account_chart_template_data.xml',
           'data/account_fiscal_position_template_data.xml',
           'data/account_data.xml',
           'data/account_tax_data.xml',
           'data/account_chart_template_configure_data.xml',
           'data/res_country_states.xml',
           'data/res.bank.csv',
           ],
}
