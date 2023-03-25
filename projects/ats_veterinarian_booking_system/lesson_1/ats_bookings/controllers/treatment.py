# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from treatment.py")


# function to log a treatment for a pet during an appointment 
def log(): 
    pet_id = request.vars.pet_id 
    appointment_id = request.vars.appointment_id 
    form = SQLFORM.factory( 
        Field('treatment_code', requires=IS_NOT_EMPTY()), 
        Field('treatment_description', requires=IS_NOT_EMPTY()), 
        Field('cost', 'decimal(10,2)', requires=IS_NOT_EMPTY()) 
    ) 

    if form.process().accepted: 
        treatment_id = add_treatment(pet_id, appointment_id, form.vars.treatment_code, form.vars.cost) 
        response.flash = f'Treatment {form.vars.treatment_code} has been logged.' 
        redirect(URL('default', 'dashboard')) 
    elif form.errors: 
        response.error = 'Please correct the errors.' 

    return {'form': form}
