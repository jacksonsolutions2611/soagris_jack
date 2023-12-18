# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Invoice With Payment from CSV File | Import Invoice With Payment From Excel file | Import Bill With Payment from CSV File | Import Bill With Payment From Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Accounting",
    "summary": "import paid invoice import bill from csv import receipt XLSX import mass invoice import bulk invoices with payment from csv import bills with payment import vendor bills import account invoice import invoices from xls customer invoice Odoo",
    "description": """This module is useful to bulk import invoices with payment details from CSV/Excel file. You can import customer invoices as well vendor bills both with payment details. Additionally, we provide the option to choose an account, account number, payment type, auto post & auto payment for import invoices with payment. So you do not need to enter records manually.""",
    "version": "15.0.1",
    "depends": [
        "sh_message",
        "account"
    ],
    "data": [
        'security/import_inv_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_inv_wizard.xml',
        'views/account_view.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "license": "OPL-1",
    "application": True,
    "auto_install": False,
    "installable": True,
    "price": 20,
    "currency": "EUR"
}
