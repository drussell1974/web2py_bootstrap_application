# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
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
        (T('Tutorials'), False, '#', [
            (T('Placeholders'), False, URL('tutorial', 'index')),
            (T('Bootstrap examples'), False, URL('tutorial', 'bootstrap_example')),
            (T('Bootstrap - Cards'), False, URL('tutorial', 'bootstrap_card')),
            (T('Bootstrap - Carousel (interactive)'), False, URL('tutorial', 'bootstrap_carousel')),
            (T('Bootstrap - Breadcrumb'), False, URL('tutorial', 'bootstrap_breadcrumb')),
            (T('Bootstrap - Buttons'), False, URL('tutorial', 'bootstrap_button')),
            (T('Bootstrap - Form (interactive)'), False, URL('tutorial', 'bootstrap_form')),
            (T('Bootstrap - Jumbotron'), False, URL('tutorial', 'bootstrap_jumbotron')),
            (T('Bootstrap - Media object'), False, URL('tutorial', 'bootstrap_mediaobject')),
            (T('Bootstrap - Modal (interactive)'), False, URL('tutorial', 'bootstrap_modal')),
            (T('Bootstrap - Navigation menu'), False, URL('tutorial', 'bootstrap_nav')),
            (T('Bootstrap - Pagination'), False, URL('tutorial', 'bootstrap_pagination')),
            (T('Bootstrap - Table'), False, URL('tutorial', 'bootstrap_table')),
        ]),
        (T('About'), False, URL(
            'admin', 'default', 'about/' + _app)),
    ]
