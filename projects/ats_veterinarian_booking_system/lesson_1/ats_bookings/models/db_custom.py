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


#== SET LISTS AVAILABLE GLOBALLY TO CONTROLLERS ==#

db_custom_speciality_list = ['Anaeshtetics', 'Bone Fractures', 'Cardiology', 'Diabetes', 'ENT', 'Epilepsy', 'Eye Conditions', 'Gastroenteroloyg', 'Genetics', 'Onocology', 'Respiratory', 'Sterilisation']
db_custom_branch_list = ['Lakeside', 'Riverside', 'Seaside']


# owner table to record owners 
db.define_table('owner',
                Field('first_name', requires=IS_NOT_EMPTY()),
                Field('last_name', requires=IS_NOT_EMPTY()),
                Field('client_branch', requires=IS_IN_SET(db_custom_branch_list))
               ) 

# client table to record clients (pets) 
db.define_table('client', 
                Field('client_name', requires=IS_NOT_EMPTY()), 
                Field('client_breed', requires=IS_NOT_EMPTY()), 
                Field('client_sex', requires=IS_IN_SET(['M', 'F'])), 
                Field('owner_id', 'reference owner')) 

# vet table to record vets 
db.define_table('vets', 
                Field('first_name', requires=IS_NOT_EMPTY()), 
                Field('last_name', requires=IS_NOT_EMPTY()), 
                Field('specialty', requires=IS_IN_SET(db_custom_speciality_list)),
                Field('home_branch', requires=IS_IN_SET(db_custom_branch_list)),
               ) 

# appointment table to record appointments 
db.define_table('appointment', 
                Field('client_id', 'reference client'), 
                Field('branch', requires=IS_IN_SET(db_custom_branch_list)), 
                Field('appointment_time', 'datetime'), 
                Field('vet_id', 'reference vets')) 

# treatment table to record treatments
db.define_table('treatment', 
                Field('treatment_code', requires=IS_NOT_EMPTY()), 
                Field('treatment_description', requires=IS_NOT_EMPTY()), 
                Field('cost', 'decimal(10,2)', requires=IS_NOT_EMPTY()))
