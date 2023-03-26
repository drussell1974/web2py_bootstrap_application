# -*- coding: utf-8 -*-
# try something like
 
def index():  

    grid = SQLFORM.grid(db.owner) 

    return dict(grid=grid) 


def edit(): 

    form = SQLFORM.factory(
        Field('first_name', requires=IS_NOT_EMPTY()),
        Field('last_name', requires=IS_NOT_EMPTY()), 
        Field('client_branch', requires=IS_IN_SET(['Lakeside', 'Seaside', 'Riverside'])),
    ) 

    if form.process().accepted:
        # insert the post variables from the from
        owner_id = db.owner.insert(
            first_name = form.vars.first_name,
            last_name = form.vars.last_name, 
            client_branch = form.vars.client_branch)

    return dict(form=form)
