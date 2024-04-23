{
    'name': "Event Management System",
    'author': 'Irene and Nick',
    'depends': ['mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/mail_template_data.xml',
        'data/mail_template_data_vip_guest.xml',
        'data/mail_template_data_speaker.xml',
        'data/mail_template_data_organizer.xml',
        'views/user.xml',
        'views/menu.xml',
        # 'views/events_attend.xml',
        'views/organizer.xml',
        'views/event.xml',
        'views/vip_guest.xml',
        'views/speaker.xml',
        'views/guest.xml'
    ]
}
