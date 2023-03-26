# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from followup.py")

# function to schedule a follow-up appointment 

def schedule(): 
    # schedule from original appointment pass appointment_id
    
    initial_appointment_id = request.vars.appointment_id 

    initial_appointment = db(db.appointment.id == initial_appointment_id).select().first() 
    vet_id = initial_appointment.vet_id
    branch = initial_appointment.branch 
    form = SQLFORM.factory(Field('appointment_time', 'datetime', requires=IS_NOT_EMPTY())) 
    
    if form.process().accepted: 
        followup_appointment_id = db.appointment.insert(client_id=initial_appointment.client_id, 
                                                           branch=branch, 
                                                           appointment_time=form.vars.appointment_time, 
                                                           vet_id=vet_id)
        response.flash = 'Follow-up appointment scheduled.' 
        redirect(URL('appointment', 'index', vars={'client_id': client_id, 'appointment_id': followup_appointment_id})) 
    elif form.errors: 
        response.error = 'Please correct the errors.' 
        
    return {'form': form}

