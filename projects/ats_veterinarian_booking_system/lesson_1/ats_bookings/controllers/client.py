# -*- coding: utf-8 -*-
# try something like

def index():
    return dict(message="hello from client.py")


def register():

    form = SQLFORM.factory(
        Field('client_name', requires=IS_NOT_EMPTY()),
        Field('client_breed', requires=IS_NOT_EMPTY()),
        Field('client_sex', requires=IS_IN_SET(['M', 'F'])),
        Field('owner_first_name', requires=IS_NOT_EMPTY()),
        Field('owner_last_name', requires=IS_NOT_EMPTY()),
        Field('owner_branch', requires=IS_IN_SET(['Lakeside', 'Seaside', 'Riverside'])),
    )

    if form.process().accepted:
        # get owner from owner table
        owner = db(db.owner.last_name == form.vars.owner_last_name and db.owner.first_name == form.vars.owner_first_name).select().first()
    
        # insert owner if they do not exist
        if owner is None:
            owner = db.owner.insert(first_name=form.vars.owner_first_name, 
                                    last_name=form.vars.owner_last_name, 
                                    owner_branch=form.vars.owner_branch)
        # insert client
        db.client.insert(client_name=form.vars.client_name, 
                          client_breed=form.vars.client_breed, 
                          client_sex=form.vars.client_sex, 
                          owner_id=owner.id) 
        
        response.flash = f'{form.vars.client_name} has been registered!'
        
    elif form.errors:
        response.error = 'Please correct the errors.'

    registered_client = SQLFORM.grid(db.client)
    
    return {'form': form, 'registered_client': registered_client }