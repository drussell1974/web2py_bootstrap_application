# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Placeholders'), False, URL('default', 'index')),
    (T('Examples'), False, '#', [
        (T('Bootstrap - Cards'), False, URL('default', 'bootstrap_card')),
        (T('Bootstrap - Carousel (interactive)'), False, URL('default', 'bootstrap_carousel')),
        (T('Bootstrap - Buttons'), False, URL('default', 'bootstrap_button')),
        (T('Bootstrap - Form (interactive)'), False, URL('default', 'bootstrap_form')),
        (T('Bootstrap - Jumbotron'), False, URL('default', 'bootstrap_jumbotron')),
        (T('Bootstrap - Media object'), False, URL('default', 'bootstrap_mediaobject')),
        (T('Bootstrap - Modal (interactive)'), False, URL('default', 'bootstrap_modal')),
        (T('Bootstrap - Navigation menu'), False, URL('default', 'bootstrap_nav')),
        (T('Bootstrap - Pagination'), False, URL('default', 'bootstrap_pagination')),
        (T('Bootstrap - Table'), False, URL('default', 'bootstrap_table')),
    ]),
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('Dashboard'), False, URL('admin', 'default', 'design/%s' % _app)),
        (T('Code'), False, '#', [
            (T('Controller'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (_app, request.controller))),
            (T('DB Model'), True,
             URL(
                 'admin', 'default', 'edit/%s/models/db_custom.py' % _app)),
            (T('Database'), False, URL(_app, 'appadmin', 'index')),
            (T('Config.ini'), False,
             URL(
                 'admin', 'default', 'edit/%s/private/appconfig.ini' % _app)),
        ]),
        (T('Presentation'), False, '#', [
            (T('View'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/%s' % (_app, response.view))),
            (T('Template'), False,
                URL(
                    'admin', 'default', 'edit/%s/views/layout.html' % _app)),
            (T('Stylesheet'), False,
                URL(
                    'admin', 'default', 'edit/%s/static/css/stylesheet.css' % _app)),
        ]),
        (T('About'), False, URL(
            'admin', 'default', 'about/' + _app)),
    ]
