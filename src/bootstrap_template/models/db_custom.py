# default database used by web2py - it will be created in the databases folder when the application if first run
# NOTE: the student will need permissions
db = DAL('sqlite://storage.sqlite')

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

db.define_table('employee_of_the_month',
    Field('name', 'string', 30),
    Field('job_role', 'string', 50),
    Field('qualities', 'text', 300),
    Field('quote', 'text', 1000),
    Field('image_path', 'string', 1000),
    # TODO: Add field for favourite film
)

