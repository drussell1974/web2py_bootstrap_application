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
    
    appointments = [] 
    
    if form.process().accepted: 
        clients = db(db.client.client_name == form.vars.client_name).select()
        
        for client in clients: 
            appointments_query = (db.appointments.client_id == client.id) 
            appointments += db(appointments_query).select() 
        if not appointments: 
            response.error = 'No appointments found.' 
        else: 
            form = SQLFORM.factory(Field('appointment_time', requires=IS_IN_DB(db, 'appointments.id', '%(appointment_time)s')), table_name='appointments') 
            form.elements('input[type=submit]')[0]['_value'] = 'Confirm Appointment'
    elif form.errors: 
        response.error = 'Please correct the errors.'

    return {'form': form, 'appointments': appointments }


# function to confirm the appointment 
def confirm(): 
    
    form = SQLFORM.factory(
        Field('appointment_time', requires=IS_IN_DB(db, 'appointments.id', '%(appointment_time)s')),
        table_name='appointments') 
    
    if form.process().accepted: 
        appointment_id = form.vars.appointment_time 
        appointment = db(db.appointments.id == appointment_id).select().first() 
        client = db(db.client.id == appointment.client_id).select().first() 
        client_id = appointment.client_id 
        vet = db(db.vets.id == vet_id).select().first() 
        
        vets = db(db.vets.specialty == specialty).select() 
        appointments_query = (db.appointments.branch == branch) & (db.appointments.appointment_time == appointment_time) 
        booked_vets = db(appointments_query).select(db.appointments.vet_id)

        for vet in vets: 
            if vet.id not in booked_vets: 
                return vet.id 
        
        if vet_id: 
            return db.appointments.insert(client_id=pet_id, 
                                           branch=branch, 
                                           appointment_time=appointment_time, 
                                           vet_id=vet_id) 
        
        response.flash = f'Appointment confirmed for {client.client_name} with Dr. {vet.last_name} on {appointment.appointment_time}.' 
        redirect(URL('default', 'dashboard')) 

    return {'form': form}
