# -*- coding: utf-8 -*-
{
    'name': "contex_integrate",

    'summary': """
        Moudlo de uso exclusivo para cliente Contex""",

    'description': """
        Moudlo de uso exclusivo para cliente Contex - Manejo de cuenta de clientes
    """,

    'author': "Librasoft",
    'website': "http://libra-soft.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_accountant', 'l10n_ar_aeroo_payment_group', 'account_debt_management', 'l10n_ar_cta_cte'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}