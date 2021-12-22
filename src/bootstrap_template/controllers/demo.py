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
    name = ""
    job_role = ""
    qualities = ""
    quote = ""
    image_path = ""
    
    # get row from database
    rows = db(db.employee_of_the_month).select()

    for row in rows:
        # set employee variables, if available - HINT: add record to employee_of_the_month table 
        name = row.name
        job_role = row.job_role
        qualities = row.qualities # Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        quote = row.quote # "Lobortis feugiat vivamus at augue eget arcu dictum varius duis. Donec adipiscing tristique risus nec. Aliquet risus feugiat in ante metus dictum at tempor. Massa tincidunt nunc pulvinar sapien. Hac habitasse platea dictumst vestibulum rhoncus est. Leo a diam sollicitudin tempor. Rhoncus dolor purus non enim praesent elementum. Ut diam quam nulla porttitor. Feugiat pretium nibh ipsum consequat nisl vel pretium lectus."
        image_path = row.image_path # "/images/placeholder/350x350.png"

    return dict(employee_name=name, employee_job_role=job_role, employee_qualities=qualities, employee_quote=quote, employee_image_path=image_path)


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
