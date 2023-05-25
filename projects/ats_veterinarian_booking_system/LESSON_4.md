# Coding the ATS Veterinarian Booking System using AI

Ask AI to create a base Web2py application based on your design. You should model this as close as possible to the design. For example, the following requests specify the relationship between each entity (table) and specify the attributes (fields), in two requests.

- *[Introducion](README.md)
- *[Lesson 1. Define the base Web2py application](LESSON_1.md)
- *[Lesson 2. Create the create_pet view](LESSON_2.md)
- *[Lesson 3. Implement Form Validation and Datatypes](LESSON_3.md)
- *[Lesson 4. Create controllers for CRUD actions for each entity](LESSON_4.md)
- *[Lesson 5. Fixing and creating relationships](LESSON_5.md)
- *[Lesson 6. Functional Testing and Boundary Testing](LESSON_6.md)
- *[Lesson 7. User Experience - Displaying values across more than one table - INNER JOIN](LESSON_7.md)
- *[Troubleshooting](TROUBLESHOOTING.md)

**IMPORTANT:**

When using AI it is best practive to keep each request in the same conversation.

# Lesson 4. Create controllers for CRUD actions for each entity #

During [Lesson 1. Define the base Web2py application](LESSON_1.md), AI created actions index, create_pet, edit_pet and delete_pet in the controllers/default.py. We put these into *controllers/pets.py*.

As stated by the AI response during lesson 1, "Similar CRUD actions can be defined for other entities (owner, appointment, treatment, vet, skill, treatment_cost)."

## 1. Ask AI to create controllers ##

Next ask AI to create the other controllers for the other entities (owner, appointment, treatment, vet, skill, treatment_cost).

**Repeat the request for each entity.**

<details>
    <summary>Click to view AI request</summary>

create controller and index view for owners just like controllers/default.py above.

</details>

<details>
    <summary>Click to view AI response</summary>
    
Certainly! Here's an example of the controller and index view for the owners entity:

controllers/owners.py
```python
Copy code
def index():
    owners = db().select(db.owner.ALL)
    return dict(owners=owners)

def create_owner():
    form = SQLFORM(db.owner)
    if form.process().accepted:
        redirect(URL('owners', 'index'))
    return dict(form=form)

def edit_owner():
    owner_id = request.args(0)
    owner = db.owner(owner_id)
    form = SQLFORM(db.owner, owner)
    if form.process().accepted:
        redirect(URL('owners', 'index'))
    return dict(form=form)

def delete_owner():
    owner_id = request.args(0)
    db(db.owner.id == owner_id).delete()
    redirect(URL('owners', 'index'))
```

views/owners/index.html
```html
Copy code
{{extend 'layout.html'}}
{{=LOAD('static', 'web2py_ajax.html')}}
<h1>Owners</h1>
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Registered Branch</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {{for owner in owners:}}
        <tr>
            <td>{{=owner.first_name}} {{=owner.last_name}}</td>
            <td>{{=owner.email}}</td>
            <td>{{=owner.phone}}</td>
            <td>{{=owner.registered_branch}}</td>
            <td>
                {{=A('Edit', _href=URL('owners', 'edit_owner', args=[owner.id]))}} |
                {{=A('Delete', _href=URL('owners', 'delete_owner', args=[owner.id]), _class='delete-btn')}}
            </td>
        </tr>
        {{pass}}
    </tbody>
</table>
{{=A('Add Owner', _href=URL('owners', 'create_owner'), _class='btn')}}

<script>
    $(document).ready(function() {
        $('.delete-btn').click(function() {
            return confirm('Are you sure you want to delete this owner?');
        });
    });
</script>
```

In the owners.py controller, you can find the CRUD actions for the owners entity similar to the previous examples. The index action retrieves all owners from the database and passes them to the index.html view.

The index.html view displays the owners in a table, showing their name, email, phone, and registered branch. It also provides options to edit or delete each owner. The view includes a form to create a new owner.

Make sure to save the owners.py file in the controllers directory and the index.html file in the views/owners directory.

</details>

## 2. Implementing the code ##

**As per the response above, create a contrroller *controllers/owners.py* and view *owners/index.html*.

controllers/owners.py
```python
Copy code
def index():
    owners = db().select(db.owner.ALL)
    return dict(owners=owners)

def create_owner():
    form = SQLFORM(db.owner)
    if form.process().accepted:
        redirect(URL('owners', 'index'))
    return dict(form=form)

def edit_owner():
    owner_id = request.args(0)
    owner = db.owner(owner_id)
    form = SQLFORM(db.owner, owner)
    if form.process().accepted:
        redirect(URL('owners', 'index'))
    return dict(form=form)

def delete_owner():
    owner_id = request.args(0)
    db(db.owner.id == owner_id).delete()
    redirect(URL('owners', 'index'))
```

views/owners/index.html
```html
Copy code
{{extend 'layout.html'}}
<h1>Owners</h1>
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Registered Branch</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {{for owner in owners:}}
        <tr>
            <td>{{=owner.first_name}} {{=owner.last_name}}</td>
            <td>{{=owner.email}}</td>
            <td>{{=owner.phone}}</td>
            <td>{{=owner.registered_branch}}</td>
            <td>
                {{=A('Edit', _href=URL('owners', 'edit_owner', args=[owner.id]))}} |
                {{=A('Delete', _href=URL('owners', 'delete_owner', args=[owner.id]), _class='delete-btn')}}
            </td>
        </tr>
        {{pass}}
    </tbody>
</table>
{{=A('Add Owner', _href=URL('owners', 'create_owner'), _class='btn')}}

<script>
    $(document).ready(function() {
        $('.delete-btn').click(function() {
            return confirm('Are you sure you want to delete this owner?');
        });
    });
</script>
```

**Show the URL to open owners/index - update views/layout.html**

Update layout.html to add the dropdown menu to execute the index action in controllers/owners.py and display the owners/index.html page

Add another list item <li class="nav-item">...</li>.

```html
Copy code
...
            <li><a class="dropdown-item" href="{{=URL('pets', 'index')}}">List</a></li>
        </ul>
    </div>
</li>

<li class="nav-item"> 
    <div id="myDropdown"> 
        <a class="nav-link text-white lead dropdown dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">Owners</a> 
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink"> 
            <li><a class="dropdown-item" href="{{=URL('owners', 'index')}}">List</a></li>
        </ul>
    </div>
</li> 
<!-- END Add menu items nav-item -->
```

**Create a view owners/create_owner.html**

1. From the site page click dashboard

2. Beneath the views (html) pages, click Create and enter 'owners/create_owner.html'.

3. Click Create below the text

4. Copy-and-paste the following html code.

NOTE: For the purpose of this tutorial we will use {{=form}} which will render it own html.

```html
{{extend 'layout.html'}}

<h1>Add Owner</h1>
{{=form}}
```

**From the Pet index page (http://127.0.0.1:8000/ats_bookings/owners/index), click Add Owner**

1. Go to the site, select Owners > List from the main menu.

2. Select Add Owners

3. Enter the First Name, Last_name, Initial, Email, Phone and Registered branch.

4. Click Add Owner

5. The implementation has limited or innaccurate functionality. 

6. After the form has submitted, you should see the record appear on the Pets index page (alternatively, select Pets > List from the main menu).

**Create a view pets/edit_pet.html**

1. From the site page click dashboard

2. Beneath the views (html) pages, click Create and enter 'owners/edit_owner.html'.

3. Click Create below the text.

4. Copy-and-paste the following html code.

NOTE: For the purpose of this tutorial we will use {{=form}} which will render it own html.

```html
{{extend 'layout.html'}}

<h1>Edit Owner</h1>
{{=form}}
```

1. Go to the site, select Owners > List from the main menu.

2. Select Edit next one of the owners you've created.

**Test the delete action**

1. Go to the site, select Owner > List from the main menu.

2. Select delete next to the owner you no longer want.

3. Click OK to confirm you want to delete.

# NEXT STEPS #

Repeat the steps above to create a controller and view for each entity.

**Ask AI, "Create controller and index view for <<ENTITY_HERE>> just like controllers/default.py above."**

Entity Name
- Appointment
- Treatment
- Vet
- Skill
- Treatment Cost

**Review entity relationships**

The generated tables (entities) do not include the correct entity relationships.

*[Lesson 5. Fixing and sCreating relationships](LESSON_5.md)

**DISCLAIMER**

Writing code requires careful consideration of various factors, such as specific requirements, best practices, and potential risks. Therefore, it is crucial to thoroughly review and test any code generated by this AI model before implementing it in a production environment. The user assumes all responsibility and liability for the usage and consequences of any code written or derived from this AI model. The AI model's responses should be used with caution and verified by human experts to ensure accuracy and suitability for the intended purpose. OpenAI, the developers of this AI model, cannot be held liable for any damages or losses resulting from the use of the generated code.

**This guide uses markdown.**

*[Markdown Guide](https://www.markdownguide.org/basic-syntax/)