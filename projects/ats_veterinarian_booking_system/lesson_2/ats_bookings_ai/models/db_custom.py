# default database used by web2py - it will be created in the databases folder when the application if first run
# NOTE: the student will need permissions
db = DAL('sqlite://storage.sqlite', fake_migrate_all=True)

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

# Owner: This table represents the owners of the pets. It will have a one-to-many relationship with the Pet table.

db.define_table('owner',
    Field('init', 'string'),
    Field('last_name', 'string'),
    Field('branch', 'string')
)

# Pet: This table represents the pets (clients) in the system. It will have a foreign key to the Owner table.

db.define_table('pet',
    Field('name', 'string'),
    Field('breed', 'string'),
    Field('sex', 'string'),
    Field('owner', 'reference owner')
)

# Vet: This table represents the veterinarians. It will have a one-to-many relationship with the Treatment table and a many-to-many relationship with the Skill table.

db.define_table('vet', 
    Field('first_name', 'string'),
    Field('last_name', 'string'),
    Field('grade', 'string'),
    Field('branch', 'string'),
    Field('extension', 'integer')
)

#Skill: This table represents the skills of veterinarians. It will have a many-to-many relationship with the Vet table.

db.define_table('skill',
    Field('name', 'string'),
    Field('skill', 'reference vet')
)

# Appointment: This table represents the appointments for pets. It will have a foreign key to the Pet table and a many-to-many relationship with the Treatment table.

db.define_table('appointment',
    Field('pet', 'reference pet'),
    Field('appointment_date', 'date'),
    Field('branch', 'string')
)

# Treatment: This table represents the treatments available. It will have a many-to-many relationship with the Appointment table and a foreign key to the Vet table.

db.define_table('treatment_cost',
    Field('description', 'string'),
    Field('cost', 'float')
)

db.define_table('treatment', 
    Field('appointment', 'reference appointment'),
    Field('vet', 'reference vet'),
    Field('cost', 'reference treatment_cost')
)
