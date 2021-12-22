# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the demo controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

def index():
    ''' the controller for the index page that shows views/demo/index.html '''

    response.title = "Home"
    
    # TODO: get current shows from table and pass current_shows variable to view
    # TODO: get future shows from table and pass coming_soon variable to view

    return dict()


def about_us():
    ''' the controller for the about page that shows views/demo/about_us.html '''
    
    response.title = "About us"
    
    return dict()


def user():
    # ---- Action for login/register/etc (required for auth) -----
    
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())
