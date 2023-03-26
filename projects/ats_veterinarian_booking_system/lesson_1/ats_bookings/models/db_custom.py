# default database used by web2py - it will be created in the databases folder when the application if first run
# NOTE: the student will need permissions
db = DAL('sqlite://storage.sqlite')

production = False
if production:
    # connect to mysql
    URI = 'mysql://<username>:<password>@<username>.mysql.eu.pythonanywhere-services.com/<username>$<database>'
    db = DAL(URI, pool_size=20, fake_migrate_all=True)

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# for test purposes only with sqlite

# owner table to list owners
db.define_table('owner',
                Field('first_name', requires=IS_NOT_EMPTY()),
                Field('last_name', requires=IS_NOT_EMPTY()),
                Field('client_branch', requires=IS_NOT_EMPTY())
               ) 

# client table to list pets and owner
db.define_table('client', 
                Field('client_name', requires=IS_NOT_EMPTY()), 
                Field('client_breed', requires=IS_NOT_EMPTY()), 
                Field('client_sex', requires=IS_IN_SET(['M', 'F'])), 
                Field('owner_id', 'reference owner')) 

# vets table to list vets and speciality 
db.define_table('vets', 
                Field('first_name', requires=IS_NOT_EMPTY()), 
                Field('last_name', requires=IS_NOT_EMPTY()), 
                Field('specialty', requires=IS_NOT_EMPTY())) 

# appointments table to record appointments 
db.define_table('appointments', 
                Field('client_id', 'reference client'), 
                Field('branch', requires=IS_NOT_EMPTY()), 
                Field('appointment_time', 'datetime'), 
                Field('vet_id', 'reference vets')) 


# function to find an available veterinarian based on specialty and branch 
def find_available_vet(specialty, branch, appointment_time): 
    vet_query = (db.vets.specialty == specialty) 
    vets = db(vet_query).select() 
    appointments_query = (db.appointments.branch == branch) & (db.appointments.appointment_time == appointment_time) 
    booked_vets = db(appointments_query).select(db.appointments.vet_id)
    
    for vet in vets: 
        if vet.id not in booked_vets: 
            return vet.id 
    return None 


# function to add a new appointment with an assigned veterinarian 
def add_appointment(client_id, branch, appointment_time, specialty): 
    vet_id = find_available_vet(specialty, branch, appointment_time) 
    if vet_id: 
        return db.appointments.insert(client_id=pet_id, 
                                       branch=branch, 
                                       appointment_time=appointment_time, 
                                       vet_id=vet_id) 
    else: 
        return None 
    
# treatments.py 

db.define_table('treatments', 
                Field('treatment_code', requires=IS_NOT_EMPTY()), 
                Field('treatment_description', requires=IS_NOT_EMPTY()), 
                Field('cost', 'decimal(10,2)', requires=IS_NOT_EMPTY())) 

# function to add a new treatment for a pet during an appointment 
def add_treatment(pet_id, appointment_id, treatment_code, cost): 
    return db.treatments.insert(pet_id=pet_id, 
                                 appointment_id=appointment_id, 
                                 treatment_code=treatment_code, 
                                 cost=cost) 


# function to add a new follow-up appointment 
def add_followup(pet_id, branch, appointment_time, vet_id): 
    return db.appointments.insert(pet_id=pet_id, 
                                   branch=branch, 
                                   appointment_time=appointment_time, 
                                   vet_id=vet_id)
