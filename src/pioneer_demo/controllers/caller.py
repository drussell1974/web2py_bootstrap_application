# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the default controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

def index():
    ''' the controller for the index page that shows views/caller/index.html '''

    response.title = "Caller"

    # TODO: Get callers from database
    raw_rows = db.executesql('get_all_callers')
    rows = db._adapter.parse(raw_rows,
        fields=[field for field in db.all_callers],
        colnames=db.all_callers.fields
    )
    # TODO: Return as table array

    return dict(rows=rows)


def view():
    ''' the controller for the about page that shows views/default/about_us.html '''
    
    response.title = "Edit"
    
    return dict()


def edit():
    ''' the controller for the about page that shows views/default/about_us.html '''
    
    response.title = "Edit"
    
    return dict()
