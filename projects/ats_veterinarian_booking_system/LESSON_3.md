# Coding the ATS Veterinarian Booking System using AI

Ask AI to create a base Web2py application based on your design. You should model this as close as possible to the design. For example, the following requests specify the relationship between each entity (table) and specify the attributes (fields), in two requests.

- *[Introducion](README.md)
- *[Lesson 1. Define the base Web2py application](LESSON_1.md)
- *[Lesson 2. Create the create_pet view](LESSON_2.md)
- *[Lesson 3. Implement Form Validation and Datatypes](LESSON_3.md)
- *[Troubleshooting](TROUBLESHOOTING.md)

**IMPORTANT:**

When using AI it is best practive to keep each request in the same conversation.

# Lesson 3. Implement Form Validation and Datatypes #

The previous implementation in lesson 2 *[Lesson 2. Create the create_pet view](LESSON_2.md)* had limited datatypes and validation on the tables defined. 

The framework uses SQLFORM with SQLite. SQLite does NOT enforce max length. 

In the next steps, you will create  *models/db_custom.py* with datatypes and validation such 

*[See Field Constructor and how to specify field type and length](http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#define_table-signature)


**Implicitly assign data types to the define_tables**

For each field in the table definitiion, the second attribute indicates the data type. If not data type is specified the field is string with maximum length of 512 characthers (or SQL type varchar(512)).

See field types for validators and default length.

*[Field Types](http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#Field-types)

```python
Field(field_name, data_type, requires)
```

**Update the field types and validation**

*Pet table/entity*

web2py: db_custom.py
```python
# Pet entity
db.define_table('pet',
                Field('name', data_type='string', requires=IS_LENGTH(maxsize=35, minsize=1)),
                Field('breed', 'string', requires=IS_NOT_EMPTY()),
                Field('sex', 'string', requires=IS_IN_SET(['M', 'F'])),
                format='%(name)s')
```
<details>
    <summary>View SQL Equivalent for Pet table</summary>

| --- | ------ | ------ | ------ |
| Field | Data Type Web2py/SQL | Validation | Is Required |
| --- | ------ | ------ | ------ | 
| name | varchar | maximum=35 | Yes |
| breed | varchar | maximum=512 (default) | Yes |
| sex | char | maximum=1 | Yes |
| --- | ------ | ------ | ------ |

```sql
CREATE TABLE pet (
    name varchar(35) not null,
    breed varchar(512) not null,
    sex char(1) not null
)
```

</details>

**From the Pet index page (http://127.0.0.1:8000/ats_bookings/pets/index), click Add Pet**

1. Go to the site, select Pets > List from the main menu.

2. Select Add Pet

3. Enter the name for more than 35 characters

4. Enter breed and select sex.

5. Click Add Pet.

You will notice a validation message below the text box.

![View Pets index page](img/ats_booking__lesson_3__pets_create_invalid_pet.png)

# Define remaining attributes tables with data types and validation #

## Owner table/entity ##

web2py: db_custom.py
```python
# Owner entity
db.define_table('owner',
                Field('first_name', 'string', requires=IS_LENGTH(maxsize=20, minsize=1)),
                Field('last_name', 'string', requires=IS_NOT_EMPTY()),
                Field('initial', 'string', length=2),
                Field('email', 'string', requires=IS_EMAIL()),
                Field('phone', 'string'),
                Field('registered_branch'),
                format='%(first_name)s %(last_name)s')
```

<details>
    <summary>View SQL Equivalent for Owner table</summary>
    

| --- | ------ | ------ | ------ |
| Field | Data Type | Validation | Is Required |
| --- | ------ | ------ | ------ | 
| first_name | string/varchar | maximum_length=20 | Yes |
| last_name | string/varchar | not null, maximum_length=20 |Yes |
| initial | string/char | not null, maximum_length=2 | Yes |
| email | string/varchar | maximum_length=256 | No |
| phone | string/varchar | maximum_length=15 | No |
| registered_branch | string/varchar | maximum_length=15 | Yes |
| --- | ------ | ------ |

```sql
CREATE TABLE owner (
    first_name varchar(35) not null,
    last_name varchar(35) not null,
    initial char(2) not null,
    email varchar(256),
    phone varchar(15),
    registered_branch varchar(15) not null
)
```

</detials>

## Appointment table/entity ##

web2py: db_custom.py
```python
# Appointment entity
db.define_table('appointment',
                Field('pet_id', 'reference pet'),
                Field('date', 'date', default=datetime.now().date(), requires=IS_DATE()),
                Field('time', 'time', default=datetime.now().time(), requires=IS_TIME()),
                Field('registered_branch'),
                format='%(date)s')
```

<details>
    <summary>View SQL Equivalent for Appointment table</summary>

| --- | ------ | ------ | ------ |
| Field | Data Type | Validation | Is Required |
| --- | ------ | ------ | ------ | 
| pet_id | int | reference pet | Yes |
| datetime | datetime | Is DateTime | Yes |
| registered_branch | string/varchar | maximum_length=15 | Yes |
| --- | ------ | ------ |

```sql
CREATE TABLE appointment (
    Field('pet_id', 'reference pet'),
    Field('date', 'date', default=datetime.now().date(), requires=IS_DATE()),
    Field('time', 'time', default=datetime.now().time(), requires=IS_TIME()),
    Field('registered_branch'),
)
```

</details>

## Vet table/entity ##

web2py: db_custom.py
```python
# Vet entity
db.define_table('vet',
                Field('first_name', requires=IS_NOT_EMPTY()),
                Field('last_name', requires=IS_NOT_EMPTY()),
                Field('grade', 'string', requires=IS_LENGTH(maxvalue=15)),
                Field('extension', 'string', requires=IS_LENGTH(minvalue=4,maxvalue=4)),
                Field('branch', 'string', requires=IS_LENGTH(minvalue=1,maxvalue=15)),
                format='%(first_name)s %(last_name)s')
```

<details>
    <summary>View SQL Equivalent for Appointment table</summary>

| --- | ------ | ------ | ------ |
| Field | Data Type | Validation | Is Required |
| --- | ------ | ------ | ------ | 
| first_name | string/varchar | maximum_length=20 | Yes |
| last_name | string/varchar | not null, maximum_length=20 |Yes |
| grade | string/char | maximum_length=15 | No |
| email | string/varchar | maximum_length=256 | No |
| phone | string/char | maximum_length=4 | Yes |
| registered_branch | string/varchar | maximum_length=15 | Yes |
| --- | ------ | ------ |

```sql
CREATE TABLE vet (
    first_name varchar(35) not null,
    last_name varchar(35) not null,
    grade varchar(15),
    phone char(4) not null,
    registered_branch varchar(15) not null
)
```
</details>

## Treatment table/entity ##

web2py: db_custom.py
```python
# Treatment entity
db.define_table('treatment',
                Field('appointment_id', 'reference appointment'),
                Field('vet_id', 'reference vet'),
                Field('description', 'text'),
                format='%(description)s')
```

<details>
    <summary>View SQL Equivalent for Appointment table</summary>

| --- | ------ | ------ | ------ |
| Field | Data Type | Validation | Is Required |
| --- | ------ | ------ | ------ | 
| appointment_id | integer/int | reference appointment | Yes |
| vet_id | integer/int | reference vet | Yes |
| description | text | maximum_length=4098 | Yes |
| --- | ------ | ------ |

SQL Equivalant
```sql
CREATE TABLE treatment (
    appointment_id int not null reference appointment,
    vet_id int not null reference vet,
    description text not null,
)
```

</details>

## Skill table/entity ##

web2py: db_custom.py
```python
# Skill entity
db.define_table('skill',
                Field('vet_id', 'reference vet'),
                Field('name', requires=IS_NOT_EMPTY()),
                format='%(name)s')
```

<details>
    <summary>View SQL Equivalent for Appointment table</summary>

| --- | ------ | ------ | ------ |
| Field | Data Type | Validation | Is Required |
| --- | ------ | ------ | ------ | 
| vet_id | integer/int | reference vet | Yes |
| name | string/varchar | maximum_length=4098 | Yes |
| --- | ------ | ------ |

```sql
CREATE TABLE skill (
    vet_id int not null reference vet,
    name varchar(256) not null,
)
```
</details>

## Treatment Cost table/entity ##

web2py: db_custom.py
```python
# Treatment Cost entity
db.define_table('treatment_cost',
                Field('description', 'text', requires=IS_NOT_EMPTY()),
                Field('cost', 'decimal(10,2)', default=Decimal('0.00')),
                format='%(description)s')
```

<details>
    <summary>View SQL Equivalent for Appointment table</summary>

| --- | ------ | ------ | ------ |
| Field | Data Type | Validation | Is Required |
| --- | ------ | ------ | ------ | 
| description | string/varchar | maximum_length=20 | Yes |
| cost | decimal(10,2) | maximum_length=20 |Yes |
| --- | ------ | ------ |

SQL Equivalant
```sql
CREATE TABLE treatment_cost (
    description text not null,
    cost decimal(10,2) not null default 0.00
)
```

</details>

# NEXT STEPS #

Now you have defined the tables/entities you can now create the views for create_* and edit_*

*[Lesson 5. Create views for Each Entity](LESSON_5.md)

**DISCLAIMER**

Writing code requires careful consideration of various factors, such as specific requirements, best practices, and potential risks. Therefore, it is crucial to thoroughly review and test any code generated by this AI model before implementing it in a production environment. The user assumes all responsibility and liability for the usage and consequences of any code written or derived from this AI model. The AI model's responses should be used with caution and verified by human experts to ensure accuracy and suitability for the intended purpose. OpenAI, the developers of this AI model, cannot be held liable for any damages or losses resulting from the use of the generated code.

**This guide uses markdown.**

*[Markdown Guide](https://www.markdownguide.org/basic-syntax/)