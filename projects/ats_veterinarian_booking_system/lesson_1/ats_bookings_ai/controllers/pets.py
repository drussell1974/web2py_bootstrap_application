
def index():
    pets = db(db.pet).select(db.pet.ALL)
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
