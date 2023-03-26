# -*- coding: utf-8 -*-
# try something like
 
def index():  

    grid = SQLFORM.grid(db.vets) 

    return dict(grid=grid)



def edit(): 

    form = SQLFORM.factory(db.vets) 

    if form.process().accepted:
        # insert the post variables from the from
        vet_id = db.vets.insert(
            first_name = form.vars.first_name,
            last_name = form.vars.last_name, 
            specialty = form.vars.specialty,
            client_branch = form.vars.home_branch)
        redirect(URL('index'))
        
    return dict(form=form)