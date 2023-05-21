# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the default controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

def index():
    ''' the controller for the index page that shows views/default/index.html '''

    response.title = "Home"

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


# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """ 
    Used to show uploaded images. DO NOT REMOVE!!!!
    Allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    
    Usage:

    <img src="{{=URL('download', args=image_path_variable )}}" 

    """

    return response.download(request, db)

