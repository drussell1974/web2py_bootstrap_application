# -*- coding: utf-8 -*-
# try something like
def index(): 
    return dict(message="hello from appointment.py")


# function to search for a pet by name or owner's name 
def book(): 
    
    form = SQLFORM.factory( 
        Field('client_name'), 
        Field('owner_last_name')
    )
    
    appointment = [] 
    
    if form.process().accepted: 
        clients = db(db.client.client_name == form.vars.client_name).select()
        
        for client in clients: 
            appointment_query = (db.appointment.client_id == client.id) 
            appointment += db(appointment_query).select() 
        if not appointment: 
            response.error = 'No appointments found.' 
        else: 
            form = SQLFORM.factory(Field('appointment_time', requires=IS_IN_DB(db, 'appointment.id', '%(appointment_time)s')), table_name='appointment') 
            form.elements('input[type=submit]')[0]['_value'] = 'Confirm Appointment'
    elif form.errors: 
        response.error = 'Please correct the errors.'

    return {'form': form, 'appointment': appointment }


def confirm(): 
    
    form = SQLFORM.factory(
        Field('appointment_time', requires=IS_IN_DB(db, 'appointment.id', '%(appointment_time)s')),
        Field('speciality', requires=IS_IN_SET('x','y','z')),
        table_name='appointment') 
    
    if form.process().accepted: 
        # get the selected appointment
        appointment_id = form.vars.appointment_time 
        appointment = db(db.appointment.id == appointment_id).select().first() 
        # get the client for the selected appointment
        client = db(db.client.id == appointment.client_id).select().first() 
        client_id = appointment.client_id 
        
        # get vets with speciality from given branch
        vets = db(db.vets.specialty == specialty).select() 
        appointment_query = (db.appointment.branch == branch) & (db.appointment.appointment_time == appointment_time) 
        booked_vets = db(appointment_query).select(db.appointment.vet_id)

        for vet in vets: 
            if vet.id not in booked_vets: 
                vet_id = vet.id 
                break
        
        if vet_id: 
            db.appointment.insert(client_id=client_id, 
                                   branch=branch, 
                                   appointment_time=appointment_time, 
                                   vet_id=vet_id) 
        
        response.flash = f'Appointment confirmed for {client.client_name} with Dr. {vet.last_name} on {appointment.appointment_time}.' 

    return {'form': form}