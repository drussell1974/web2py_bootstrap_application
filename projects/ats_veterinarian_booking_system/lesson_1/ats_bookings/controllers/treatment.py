# -*- coding: utf-8 -*-
# try something like
def index(): 
    client_id = request.vars.client_id 
    
    grid = SQLFORM.grid(db.treatment) 

    return dict(grid=grid) 


# function to log a treatment for a pet during an appointment 
def log(): 
    # TODO: create treatment and treatment cost table
    client_id = request.vars.client_id 
    appointment_id = request.vars.appointment_id 
    form = SQLFORM.factory( 
        Field('treatment_code', requires=IS_NOT_EMPTY()), 
        Field('treatment_description', requires=IS_NOT_EMPTY()), 
        Field('cost', 'decimal(10,2)', requires=IS_NOT_EMPTY()) 
    ) 

    if form.process().accepted: 
        db.treatment.insert(appointment_id=appointment_id,
                            treatment_code=form.vars.treatment_code,
                            cost=form.vars.cost) 
        # TODO: insert into create treatment and treatment cost table

        response.flash = f'Treatment {form.vars.treatment_code} has been logged.' 
        redirect(URL('index', vars=dict(client_id=client_id)))
        
    elif form.errors: 
        response.error = 'Please correct the errors.' 

    return {'form': form}
