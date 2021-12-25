# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the default controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

def index():
    ''' the controller for the index page that shows views/default/index.html '''

    response.title = "Home"

    # TODO: get current shows from table and pass current_shows variable to view
    # TODO: get future shows from table and pass coming_soon variable to view

    return dict()


def about_us():
    ''' the controller for the about page that shows views/default/about_us.html '''
    
    response.title = "About us"
    
    return dict()


def tickets_and_prices():
    ''' the controller for the tickets_and_prices page that shows views/default/tickets_and_prices.html '''
    
    response.title = "Tickets and Prices"

    # get tickets_and_prices from table in database
    # TODO: Create tickets_and_prices table in db_custom.py with fields name, about, price
    # TODO: Add rows to show prices for standard seating, VIP seating. 
    # TODO: Get db(db.tickets_and_prices).select()
    # TODO: In the controller set variables and pass to view: return dict(a="xyz", b="abc", c=tickets_and_prices)
    # TODO: In the tickets_and_prices.html create for loop for each row

    return dict()


def contact_us():
    ''' the controller for the contact us page that shows views/default/contact_us.html '''
    
    response.title = "Contact us"

    # get management teams from table in database
    # TODO: Create management_team table in db_custom.py with fields name, job_role, about, image_path - For image_path use datatype upload)
    # TODO: Get db(db.management_team).select()
    # TODO: In the controller set variables and pass to view: return dict(a="xyz", b="abc", c=management_team_rows)
    # TODO: In the contact_us.html view use {{=URL('download', args=image_path)}} to show the image from the table

    # if form is posted
    if request.post_vars:
        # TODO: create table customer_query with fields email_address and message in db_custom.property
        # TODO: get request email_address and message - request.post_vars.email_address and request.post_vars.message
        # TODO: save to customer_query table - customer_query.insert(email_address=request.post_vars.email_address, message=request.post_vars.message)
        pass

    return dict()


def employee_of_the_month():
    ''' the controller for the about page that shows views/default/employee_of_the_month.html '''

    response.title = "Employee of the month"

    # get row from employee_of_the_month table in database - created in db_custom.py
    rows = db(db.employee_of_the_month).select()
    
    # return rows to employee_of_the_month.html view
    return dict()


# TODO: Visitor must login - @auth.requires_login()
def members_area():
    ''' the controller for the members_area page that shows views/default/members_area.html '''
    
    response.title = "Members area"

    # get tickets_and_prices from table in database
    # TODO: Create tickets_and_prices table in db_custom.py with fields name, about, price, member_price
    # TODO: Add rows to show prices for standard seating, VIP seating. 
    # TODO: Get db(db.tickets_and_prices).select()
    # TODO: In the controller set variables and pass to view: return dict(a="xyz", b="abc", c=tickets_and_prices)
    # TODO: In the tickets_and_prices.html create for loop for each row

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
