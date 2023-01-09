# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the vehicle controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

from vehicle import Vehicle, VehicleDAL


def index():
    ''' the controller for the index page that shows views/vehicle/index.html '''

    response.title = "Vehicle - List"

    vehicle_rows = VehicleDAL.get_all(db)

    return dict(rows=vehicle_rows)


def view():
    ''' the controller for the view page that shows views/vehicle/view.html '''

    # set page (browser tab) title
    response.title = "Vehicle - View"

    if len(request.args) > 0:
        # fetch vehicle from database

        vehicle = VehicleDAL.get_by_id(db, request.args[0]) or redirect(URL('index'))

    features_rows = [] # FeatureDAL.get_all(db)

    return dict(item=vehicle, feature_rows=features_rows)


def edit():
    ''' the controller for the edit page that shows views/Vehicle/edit.html '''

    # new object
    vehicle = Vehicle.NEW()

    # check for post request

    if len(request.vars) > 0:

        vehicle = Vehicle(request.vars.id, request.vars.registration_no)

        # save
        VehicleDAL.upsert(db, vehicle)

        # goto index page
        redirect(URL('index'))


    # set page (browser tab) title
    response.title = "Vehicle - Edit"

    if len(request.args) > 0:
        # fetch customer from database

        vehicle = VehicleDAL.get_by_id(db, request.args[0])

    return dict(item=vehicle)


def delete():
    ''' the controller for the delete page redirects views/vehicle/index.html '''

    # new object
    obj = Vehicle.NEW()

    # check for post request
    if len(request.args) > 0:

        obj = Vehicle(request.args[0], request.args[0])

        VehicleDAL.delete(db, obj)

    redirect(URL('index'))
