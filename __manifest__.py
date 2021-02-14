{
    'name': "HR Salary Rule Datetime Library",

    'summary': """
Add support for standard Python datetime libraries in salary rules""",

    'summary_vi_VN': """
Hỗ trợ các thư viện datetime tiêu chuẩn của Python trong Salary Rules 
    	""",

    'description': """
What it does
============
This module adds support for the following extra libraries for usage in salary rules Python code

1. datetime
2. dateutil
3. odoo.fields

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Ứng dụng này làm gì
===================
Ứng dụng này cung cấp thêm các thư viện datetime sau đây để có thể sử dụng trong mã Python của quy tắc lương

1. datetime
2. dateutil
3. odoo.fields

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "T.V.T Marine Automation (aka TVTMA),Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v12demo-int.erponline.vn",
    'support': "apps.support@viindoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_payroll'],

    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
