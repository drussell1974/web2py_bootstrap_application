# -*- coding: utf-8 -*-
# try something like

def index():
    return dict(message="hello from pet.py")


def register():

    form = SQLFORM.factory(
        Field('pet_name', requires=IS_NOT_EMPTY()),
        Field('pet_breed', requires=IS_NOT_EMPTY()),
        Field('pet_sex', requires=IS_IN_SET(['M', 'F'])),
        Field('client_name', requires=IS_NOT_EMPTY()),
        Field('client_branch', requires=IS_IN_SET(['Lakeside', 'Seaside', 'Riverside'])),
    )

    if form.process().accepted:
        print(form.vars)
        pet_id = add_pet(form.vars.pet_name, form.vars.pet_breed, form.vars.pet_sex, form.vars.client_name, form.vars.client_branch)
        response.flash = f'{form.vars.pet_name} has been registered!'
        redirect(URL('default', 'index'))
    elif form.errors:
        response.error = 'Please correct the errors.'

    return {'form': form, 'registered_pets': db(db.pets).select() }
