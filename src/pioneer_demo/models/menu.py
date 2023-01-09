<<<<<<< HEAD
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
        (T('About'), False, URL(
            'admin', 'default', 'about/' + _app)),
    ]
=======
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
        (T('About'), False, URL(
            'admin', 'default', 'about/' + _app)),
    ]
>>>>>>> b6cfd75fb0108bc951d3af8d26556cc54b8e1568
