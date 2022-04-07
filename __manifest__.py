# -*- coding: utf-8 -*-
{
    'name': "shf_tecnic_test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_module_category_data.xml',
        'data/res_groups_data.xml',
        'data/service_category_data.xml',
        'data/ir_sequence_data.xml',
        'data/mail_template_data.xml',
        'reports/guide_detail_report.xml',
        'wizards/send_invoice_wizard.xml',
        'views/menu_views.xml',
        'views/service_category_views.xml',
        'views/service_guide_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
