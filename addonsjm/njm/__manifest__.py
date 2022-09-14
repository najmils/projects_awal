# -*- coding: utf-8 -*-
{
    'name': "njm",

    'summary': """
        odoo module for njm store""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 06 Sept 2022 sesi 1 (penambahan 'report xlsx')
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/kelompokBarang_view.xml',
        # Perubahannya ada di sini
        'views/barang_view.xml',
        # 31 Agustus 2022 sesi 1
        'views/person_view.xml',
        'views/kasir_view.xml',
        'views/konsumen_view.xml',
        'views/member_view.xml',
        'views/supplier_view.xml',
        'views/direksi_view.xml',
        'views/penjualan_view.xml',
        # 06 Sept 2022 sesi 1
        'report/report.xml',
        # 07 sept sesi 1
        'wizzard/barangdatang_wizzard_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
