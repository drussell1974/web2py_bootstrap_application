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

db.define_table('clients',
                Field('name', requires=IS_NOT_EMPTY())
                )

db.define_table('pets', 
                Field('pet_name', requires=IS_NOT_EMPTY()), 
                Field('pet_breed', requires=IS_NOT_EMPTY()), 
                Field('pet_sex', requires=IS_IN_SET(['M', 'F'])), 
                Field('client_id', 'reference clients')) 

def add_pet(pet_name, pet_breed, pet_sex, client_id): 
    return db.pets.insert(pet_name=pet_name, 
                          pet_breed=pet_breed, 
                          pet_sex=pet_sex, 
                          client_id=client_id) 


# appointments table to record appointments 
db.define_table('appointments', 
                Field('pet_id', 'reference pets'), 
                Field('branch', requires=IS_NOT_EMPTY()), 
                Field('appointment_time', 'datetime'), 
                Field('vet_id', 'reference vets')) 

# function to add a new appointment 
def add_appointment(pet_id, branch, appointment_time, vet_id): 
    return db.appointments.insert(pet_id=pet_id, branch=branch, appointment_time=appointment_time, vet_id=vet_id)


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
def add_appointment(pet_id, branch, appointment_time, specialty): 
    vet_id = find_available_vet(specialty, branch, appointment_time) 
    if vet_id: 
        return db.appointments.insert(pet_id=pet_id, 
                                       branch=branch, 
                                       appointment_time=appointment_time, 
                                       vet_id=vet_id) 
    else: 
        return None 
    