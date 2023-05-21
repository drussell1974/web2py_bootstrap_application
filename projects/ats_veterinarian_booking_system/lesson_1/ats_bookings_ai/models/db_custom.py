from datetime import datetime
from decimal import Decimal

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

# Pet entity
db.define_table('pet',
                Field('name', 'string', requires=IS_NOT_EMPTY()),
                Field('breed', 'string', requires=IS_NOT_EMPTY()),
                Field('sex', 'string', requires=IS_IN_SET(['M', 'F'])),
                format='%(name)s')

# Owner entity
db.define_table('owner',
                Field('first_name', 'string', requires=IS_NOT_EMPTY()),
                Field('last_name', 'string', requires=IS_NOT_EMPTY()),
                Field('initial', 'string', length=2),
                Field('email', 'string', requires=IS_EMAIL()),
                Field('phone', 'integer'),
                Field('registered_branch'),
                format='%(first_name)s %(last_name)s')

# Appointment entity
db.define_table('appointment',
                Field('pet_id', 'integer', 'reference pet'),
                Field('date', 'date', default=datetime.now().date(), requires=IS_DATE()),
                Field('time', 'time', default=datetime.now().time(), requires=IS_TIME()),
                Field('registered_branch'),
                format='%(date)s')

# Vet entity
db.define_table('vet',
                Field('first_name', 'string', requires=IS_NOT_EMPTY()),
                Field('last_name', 'string', requires=IS_NOT_EMPTY()),
                Field('grade', 'string'),
                Field('branch', 'string'),
                Field('extension', 'string'),
                format='%(first_name)s %(last_name)s')

# Treatment entity
db.define_table('treatment',
                Field('appointment_id', 'reference appointment'),
                Field('vet_id', 'reference vet'),
                Field('description', 'text'),
                format='%(description)s')

# Skill entity
db.define_table('skill',
                Field('vet_id', 'reference vet'),
                Field('name', 'string', requires=IS_NOT_EMPTY()),
                format='%(name)s')

# Treatment Cost entity
db.define_table('treatment_cost',
                Field('description', 'text', requires=IS_NOT_EMPTY()),
                Field('cost', 'decimal(10,2)', default=Decimal('0.00')),
                format='%(description)s')
