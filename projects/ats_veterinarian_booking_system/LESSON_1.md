# Coding the ATS Veterinarian Booking System using AI

Ask AI to create a base Web2py application based on your design. You should model this as close as possible to the design. For example, the following requests specify the relationship between each entity (table) and specify the attributes (fields), in two requests.

- *[Introducion](README.md)
- *[Lesson 1. Define the base Web2py application](LESSON_1.md)
- *[Lesson 2. Create the create_pet view](LESSON_2.md)
- *[Lesson 3. Implement Form Validation and Datatypes](LESSON_3.md)
- *[Troubleshooting](TROUBLESHOOTING.md)

**IMPORTANT:**

When using AI it is best practive to keep each request in the same conversation.

# Lesson 1. Define the base Web2py application #

![ATS Booking Design - 3NF ERD](./img/ats_booking__erd.png)

NOTE: Establish a starting point as close as possible to your solution will save time later. For example, you will need Create, Read, Update and Delete actions for each entity (table) and specify attribute (field) names.

## 1. Create application describing relationships and ask it to include CRUD actions for each entity. ##

<details>
    <summary>Click to view AI request</summary>

Create Web2py MVC application for ATS Veternarian Booking System with pet (client) has one to many owners, pet can have none to many appointments,  an appointment can have zero to many treatments, a vet and prescribe zero to many treatments, a vet can have one to many skills, and a treatment cost can have one to many treatments.

Include CRUD action for each entity.

</details>

<details>
    <summary>Click to view AI response</summary>

Sure! I can provide you with an example of a web2py MVC application for an ATS Veterinary Booking System with the mentioned entities and their relationships. Here's the code:

### models/db.py ###

```python
from datetime import datetime
from decimal import Decimal

db = DAL('sqlite://storage.sqlite')

# Pet entity
db.define_table('pet',
                Field('name', requires=IS_NOT_EMPTY()),
                Field('species', requires=IS_NOT_EMPTY()),
                format='%(name)s')

# Owner entity
db.define_table('owner',
                Field('name', requires=IS_NOT_EMPTY()),
                Field('email', requires=IS_EMAIL()),
                Field('phone'),
                format='%(name)s')

# Appointment entity
db.define_table('appointment',
                Field('pet_id', 'reference pet'),
                Field('date', 'date', default=datetime.now().date(), requires=IS_DATE()),
                format='%(date)s')

# Treatment entity
db.define_table('treatment',
                Field('appointment_id', 'reference appointment'),
                Field('vet_id', 'reference vet'),
                Field('description', 'text'),
                format='%(description)s')

# Vet entity
db.define_table('vet',
                Field('name', requires=IS_NOT_EMPTY()),
                format='%(name)s')

# Skill entity
db.define_table('skill',
                Field('vet_id', 'reference vet'),
                Field('name', requires=IS_NOT_EMPTY()),
                format='%(name)s')

# Treatment Cost entity
db.define_table('treatment_cost',
                Field('name', requires=IS_NOT_EMPTY()),
                Field('cost', 'decimal(10,2)', default=Decimal('0.00')),
                format='%(name)s')
```

### controllers/default.py ###
```python
def index():
    pets = db().select(db.pet.ALL)
    return dict(pets=pets)

def create_pet():
    form = SQLFORM(db.pet)
    if form.process().accepted:
        redirect(URL('index'))
    return dict(form=form)

def edit_pet():
    pet_id = request.args(0)
    pet = db.pet(pet_id)
    form = SQLFORM(db.pet, pet)
    if form.process().accepted:
        redirect(URL('index'))
    return dict(form=form)

def delete_pet():
    pet_id = request.args(0)
    db(db.pet.id == pet_id).delete()
    redirect(URL('index'))
```

# Similar CRUD actions can be defined for other entities (owner, appointment, treatment, vet, skill, treatment_cost).

### views/default/index.html ###

```html
{{extend 'layout.html'}}
{{=LOAD('static', 'web2py_ajax.html')}}
<h1>Pets</h1>
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Species</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {{for pet in pets:}}
        <tr>
            <td>{{=pet.name}}</td>
            <td>{{=pet.species}}</td>
            <td>
                {{=A('Edit', _href=URL('edit_pet', args=[pet.id]))}} |
                {{=A('Delete', _href=URL('delete_pet', args=[pet.id]), _class='delete-btn')}}
            </td>
        </tr>
        {{pass}}
    </tbody>
</table>
{{=A('Add Pet', _href=URL('create_pet'), _class='btn')}}

<script>
    $(document).ready(function() {
        $('.delete-btn').click(function() {
            return confirm('Are you sure you want to delete this pet?');
        });
    });
</script>
```

Make sure to have the required web2py

</details>

## 2. Specify the attribute (field) names for each entity. ##

NOTE: State the name of each entity (as stated in the previous request) and name each attribute in the following format for each entity: <entity_name> entity has attributes <attr_1>, <attr_2>, and <attr_3>.

<details>
    <summary>Click to view AI request</summary>

owner entity has attributes initial, last name and registered branch. pet entity has name, breed and sex M or F. appointment entity has attributes date, time, registered branch. vet skill entity has attribute name. vet entity has attributes first name, last name, grade, branch, extension. treatment cost entity has attributes description and cost.

</details>

<details>
    <summary>Click to view AI response</summary>

Based on the additional attributes provided, here's an updated version of the code:

### models/db.py ###

```python
from datetime import datetime
from decimal import Decimal

db = DAL('sqlite://storage.sqlite')

# Pet entity
db.define_table('pet',
                Field('name', requires=IS_NOT_EMPTY()),
                Field('breed', requires=IS_NOT_EMPTY()),
                Field('sex', 'string', requires=IS_IN_SET(['M', 'F'])),
                format='%(name)s')

# Owner entity
db.define_table('owner',
                Field('first_name', requires=IS_NOT_EMPTY()),
                Field('last_name', requires=IS_NOT_EMPTY()),
                Field('initial', 'string', length=2),
                Field('email', requires=IS_EMAIL()),
                Field('phone'),
                Field('registered_branch'),
                format='%(first_name)s %(last_name)s')

# Appointment entity
db.define_table('appointment',
                Field('pet_id', 'reference pet'),
                Field('date', 'date', default=datetime.now().date(), requires=IS_DATE()),
                Field('time', 'time', default=datetime.now().time(), requires=IS_TIME()),
                Field('registered_branch'),
                format='%(date)s')

# Treatment entity
db.define_table('treatment',
                Field('appointment_id', 'reference appointment'),
                Field('vet_id', 'reference vet'),
                Field('description', 'text'),
                format='%(description)s')

# Vet entity
db.define_table('vet',
                Field('first_name', requires=IS_NOT_EMPTY()),
                Field('last_name', requires=IS_NOT_EMPTY()),
                Field('grade'),
                Field('branch'),
                Field('extension'),
                format='%(first_name)s %(last_name)s')

# Skill entity
db.define_table('skill',
                Field('vet_id', 'reference vet'),
                Field('name', requires=IS_NOT_EMPTY()),
                format='%(name)s')

# Treatment Cost entity
db.define_table('treatment_cost',
                Field('description', requires=IS_NOT_EMPTY()),
                Field('cost', 'decimal(10,2)', default=Decimal('0.00')),
                format='%(description)s')
```

### controllers/default.py ###
# CRUD actions for each entity remain the same, just the field names have been updated.

### views/default/index.html ###
# The table header and body fields can be updated based on the new attributes.

```html
{{extend 'layout.html'}}
{{=LOAD('static', 'web2py_ajax.html')}}
<h1>Pets</h1>
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Breed</th>
            <th>Sex</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {{for pet in pets:}}
        <tr>
            <td>{{=pet.name}}</td>
            <td>{{=pet.breed}}</td>
            <td>{{=pet.sex}}</td>
            <td>
                {{=A('Edit', _href=URL('edit_pet', args=[pet.id]))}} |
                {{=A('Delete', _href=URL('delete_pet', args=[pet.id]), _class='delete-btn')}}
            </td>
        </tr>
        {{pass}}
    </tbody>
</table>
{{=A('Add Pet', _href=URL('create_pet'), _class='btn')}}

<script>
    $(document).ready(function() {
        $('.delete-btn').click(function() {
            return confirm('Are you sure you want to delete this pet?');
        });
    });
</script>
```

Please note that only the provided attributes have been included in the code, and you can add more

</details>

## 3. Implementing the code ##

**Modify models/db_custom.py**
Add the code to then end of the file

```
# Pet entity
db.define_table('pet',
                Field('name', requires=IS_NOT_EMPTY()),
                Field('breed', requires=IS_NOT_EMPTY()),
                Field('sex', 'string', requires=IS_IN_SET(['M', 'F'])),
                format='%(name)s')

# Owner entity
db.define_table('owner',
                Field('first_name', requires=IS_NOT_EMPTY()),
                Field('last_name', requires=IS_NOT_EMPTY()),
                Field('initial', 'string', length=2),
                Field('email', requires=IS_EMAIL()),
                Field('phone'),
                Field('registered_branch'),
                format='%(first_name)s %(last_name)s')

# Appointment entity
db.define_table('appointment',
                Field('pet_id', 'reference pet'),
                Field('date', 'date', default=datetime.now().date(), requires=IS_DATE()),
                Field('time', 'time', default=datetime.now().time(), requires=IS_TIME()),
                Field('registered_branch'),
                format='%(date)s')

# Vet entity
db.define_table('vet',
                Field('first_name', requires=IS_NOT_EMPTY()),
                Field('last_name', requires=IS_NOT_EMPTY()),
                Field('grade'),
                Field('branch'),
                Field('extension'),
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
                Field('name', requires=IS_NOT_EMPTY()),
                format='%(name)s')

# Treatment Cost entity
db.define_table('treatment_cost',
                Field('description', requires=IS_NOT_EMPTY()),
                Field('cost', 'decimal(10,2)', default=Decimal('0.00')),
                format='%(description)s')
```

**Create a new controller for pets - controllers/pets.py**

```python
Copy code

def index():
    pets = db().select(db.pet.ALL)
    return dict(pets=pets)

def create_pet():
    form = SQLFORM(db.pet)
    if form.process().accepted:
        redirect(URL('index'))
    return dict(form=form)

def edit_pet():
    pet_id = request.args(0)
    pet = db.pet(pet_id)
    form = SQLFORM(db.pet, pet)
    if form.process().accepted:
        redirect(URL('index'))
    return dict(form=form)

def delete_pet():
    pet_id = request.args(0)
    db(db.pet.id == pet_id).delete()
    redirect(URL('index'))
```

**Create a view for listing pets - /pets/index.html**

The HTML should be placed beneath the carousel.

![Create View create_pet.html](img/ats_booking__lesson_1__create_view_pets_index.png)

```html 
Copy code
{{extend 'layout.html'}}

<h1>Pets</h1>
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Breed</th>
            <th>Sex</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {{for pet in pets:}}
        <tr>
            <td>{{=pet.name}}</td>
            <td>{{=pet.breed}}</td>
            <td>{{=pet.sex}}</td>
            <td>
                {{=A('Edit', _href=URL('edit_pet', args=[pet.id]))}} |
                {{=A('Delete', _href=URL('delete_pet', args=[pet.id]), _class='delete-btn')}}
            </td>
        </tr>
        {{pass}}
    </tbody>
</table>
{{=A('Add Pet', _href=URL('create_pet'), _class='btn')}}

<script>
    $(document).ready(function() {
        $('.delete-btn').click(function() {
            return confirm('Are you sure you want to delete this pet?');
        });
    });
</script>
```

NOTE 1: Existing files may already include {{extend layout.html}}, and {{=LOAD('static', 'web2py_ajax.html')}} may already be included in the layout.html

**Show the URL to open pets/index - update views/layout.html**

Update layout.html to add the dropdown menu to execute the index action in controllers/pets.py and display the pets/index.html page

```html
Copy code
<!-- Add menu items nav-item -->
<li class="nav-item"> 
    <div id="myDropdown"> 
        <a class="nav-link text-white lead dropdown dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">Pets</a> 
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink"> 
            <li><a class="dropdown-item" href="{{=URL('pets', 'index')}}">List</a></li>
        </ul>
    </div>
</li> 
<!-- END Add menu items nav-item -->
```

![Create View create_pet.html](img/ats_booking__lesson_1__create_view_pets_index.png)

## 4. Open the Home Page

1. Select the menu *Pets > list*
2. Shows the empty page
3. Click Create Pet
4. If you click the 'Add Pet' link at the bottom of the page, you will get an error 'invalid view (pets/create_pet.html)'. 

![Pets Index Page](./img/ats_booking__lesson_1__pets_index_page.png)

# NEXT STEPS #

AI did not generate the code for the create_pet.html,

*[Lesson 2. Create the create_pet view](LESSON_2.md)

**DISCLAIMER**

Writing code requires careful consideration of various factors, such as specific requirements, best practices, and potential risks. Therefore, it is crucial to thoroughly review and test any code generated by this AI model before implementing it in a production environment. The user assumes all responsibility and liability for the usage and consequences of any code written or derived from this AI model. The AI model's responses should be used with caution and verified by human experts to ensure accuracy and suitability for the intended purpose. OpenAI, the developers of this AI model, cannot be held liable for any damages or losses resulting from the use of the generated code.

**This guide uses markdown.**

*[Markdown Guide](https://www.markdownguide.org/basic-syntax/)