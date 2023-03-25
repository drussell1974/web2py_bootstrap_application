# -*- coding: utf-8 -*-
# try something like
def index(): 
    return dict(message="hello from appointment.py")


# function to search for a pet by name or owner's name 
def book(): 
    
    form = SQLFORM.factory( 
        Field('pet_name'), 
        Field('owner_name') 
    ) 
    
    appointments = [] 

    if form.process().accepted: 
        pet_query = (db.pets.pet_name.contains(form.vars.pet_name)) & (db.clients.first_name.contains(form.vars.owner_name)) 
        pets = db(pet_query).select() 

        for pet in pets: 
            appointments_query = (db.appointments.pet_id == pet.id) 
            appointments += db(appointments_query).select() 
        if not appointments: 
            response.error = 'No appointments found.' 
        else: 
            form = SQLFORM.factory(Field('appointment_time', requires=IS_IN_DB(db, 'appointments.id', '%(appointment_time)s')), table_name='appointments') 
            form.elements('input[type=submit]')[0]['_value'] = 'Confirm Appointment'
    elif form.errors: 
        response.error = 'Please correct the errors.'

    return {'form': form, 'appointments': appointments}