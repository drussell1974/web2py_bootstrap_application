# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the default controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

def index():
    ''' the controller for the index page that shows views/default/index.html '''

    response.title = "Home"

    return dict()


def about_us():
    ''' the controller for the about page that shows views/default/about_us.html '''
    
    response.title = "About us"
    
    return dict()


def tickets_and_prices():
    ''' the controller for the tickets_and_prices page that shows views/default/tickets_and_prices.html '''
    
    response.title = "Tickets and Prices"

    return dict()


def contact_us():
    ''' the controller for the contact us page that shows views/default/contact_us.html '''
    
    response.title = "Contact us"

    return dict()


def employee_of_the_month():
    ''' the controller for the about page that shows views/default/employee_of_the_month.html '''

    response.title = "Employee of the month"

    # get row from employee_of_the_month table in database - created in db_custom.py
    rows = db(db.employee_of_the_month).select()
    
    # return rows to employee_of_the_month.html view
    return dict(employee_of_the_month_rows=rows)


def members_area():
    ''' the controller for the members_area page that shows views/default/members_area.html '''
    
    response.title = "Members area"

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
