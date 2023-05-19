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

    <img src="{{=URL('download', args=image_path_variable )}}">

    """

    return response.download(request, db)

# Now that we have defined our database tables, we can create the controllers and views for our web application. For brevity, I'll provide only the basic structure.

def index():
    owner_id = request.vars.owner_id
    pets = db(db.pet.owner == owner_id).select(db.pet.ALL)
    return dict(owner_id=owner_id, pets=pets)


def pets():
    # Logic to handle pets
    return dict()


def register_pet(): 

    owners = db(db.owner).select() # Retrieve all owners

    form = SQLFORM(db.pet)
    if form.process().accepted:
        pet_id = form.vars.id
        owner_id = request.vars.owner # change owner_id to owner
        db.pet.insert(pet=pet_id, owner=owner_id)
        response.flash = "Pet registered successfully!"
        
    return dict(form=form, owners=owners) # return owners in the dictionary


def owners():
    # Logic to handle owners
    return dict()


def register_owner():
    form = SQLFORM(db.owner)
    if form.process().accepted:
        response.flash = "Owner registered successfully!"
    return dict(form=form)


def appointments():
    # Logic to handle appointments
    return dict()


def treatments():
    # Logic to handle treatments
    return dict()


def vets():
    # Logic to handle vets
    return dict()


def skills():
    # Logic to handle skills
    return dict()
