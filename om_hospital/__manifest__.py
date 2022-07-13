# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Hospital Management Software
        """,

    'description': """
        Hospital Management Software
    """,

    'author': "Rivo Manana",
    'website': "http://www.rivo.com",
    'category': 'Productivity',
    'version': '14.0',
    'depends': ['base','sale','mail','account','report_xlsx'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/sale.xml',
        'views/partner.xml',
        'data/data.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',
        'report/report.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
