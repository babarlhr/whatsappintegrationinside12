# -*- coding: utf-8 -*-
{
    'name': 'Eldo Customization',
    'category': 'General',
    'summary': 'Eldo Customization',
    'version': '1.0.0',
    'author':  '',
    'website': '',
    'depends': [
        'base', 'mail', 'helpdesk', 'web'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_data.xml',
        'data/helpdesk_stage_data.xml',
        'views/templates.xml',
        'views/ewallet_view.xml',
        'views/meter_account_view.xml',
        'views/mdms_server_view.xml',
        'views/meters_view.xml',
        'views/tarrifs_view.xml',
        'views/helpdesk_ticket_type_view.xml',
        'views/helpdesk_ticket_views.xml',
    ],
    'qweb': [
        'static/src/xml/template.xml'
    ],
    'installable': True,
}
