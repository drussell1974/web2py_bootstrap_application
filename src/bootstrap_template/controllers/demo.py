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


def employee_of_the_month():
    ''' the controller for the about page that shows views/demo/about_us.html '''

    response.title = "Employee of the month"

    # create default employee of the month variables
    image_path = ""
    name = ""
    job_role = ""
    qualities = ""
    quote = ""
    # TODO: show employee's favourite film - HINT: create variable
    
    # get row from employee_of_the_month table in database - created in db_custom.py
    rows = db(db.employee_of_the_month).select()

    for row in rows:
        # set employee variables, if available - HINT: add record to employee_of_the_month table 
        image_path = row.image_path
        name = row.name
        job_role = row.job_role
        qualities = row.qualities 
        quote = row.quote
        
    return dict(employee_image_path=image_path, employee_name=name, employee_job_role=job_role, employee_qualities=qualities, employee_quote=quote)


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
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    print("this is the download")
    
    return response.download(request, db)
