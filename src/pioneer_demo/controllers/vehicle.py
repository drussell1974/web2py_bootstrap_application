# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the vehicle controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

from vehicle import Vehicle, VehicleDAL
from engine import Engine, EngineDAL
from body import Body, BodyDAL
from furnishing import Furnishing, FurnishingDAL

def index():
    ''' the controller for the index page that shows views/vehicle/index.html '''

    response.title = "Vehicle - List"

    vehicle_rows = VehicleDAL.get_all(db)

    return dict(rows=vehicle_rows)


def view():
    ''' the controller for the view page that shows views/vehicle/view.html '''

    arg_registration_no = request.args[0].replace('_', ' ')

    # set page (browser tab) title
    response.title = "Vehicle - View"

    if len(request.args) > 0:
        # fetch vehicle from database

        vehicle = VehicleDAL.get_by_id(db, arg_registration_no)

    return dict(item=vehicle)


def edit():
    ''' the controller for the edit page that shows views/vehicle/edit.html '''
    
    # new object
    vehicle = Vehicle.NEW()
    
    # check for post request

    if len(request.vars) > 0:

        vehicle = Vehicle(request.vars.id, request.vars.registration_no)
        
        engine = map(Engine.NEW, request.vars.engine_id) # pass checked values to Engine.NEW()
        vehicle.engine = engine

        body = map(Engine.NEW, request.vars.body_id) # pass checked values to Body.NEW()
        vehicle.body = body
        
        furnishing = map(Engine.NEW, request.vars.furnishing_id) # pass checked values to Furnishing.NEW()
        vehicle.furnishing = furnishing

        # save
        VehicleDAL.upsert(db, vehicle)
        EngineDAL.insert_for_vehicle(db, vehicle)
        BodyDAL.insert_for_vehicle(db, vehicle)
        FurnishingDAL.insert_for_vehicle(db, vehicle)

        # goto index page
        redirect(URL('index'))


    # set page (browser tab) title
    response.title = "Vehicle - Edit"

    arg_registration_no = request.args[0].replace('_', ' ')

    if len(request.args) > 0:
        # fetch customer from database

        vehicle = VehicleDAL.get_by_id(db, arg_registration_no)
        
        engine = EngineDAL.get_for_vehicle(db, vehicle)
        vehicle.engine = engine

        body = BodyDAL.get_for_vehicle(db, vehicle)        
        vehicle.body = body

        furnishing = FurnishingDAL.get_for_vehicle(db, vehicle)
        vehicle.furnishing = furnishing
    
    engine_all = EngineDAL.get_all(db)
    body_all = BodyDAL.get_all(db)
    furnishing_all = FurnishingDAL.get_all(db)
    
    return dict(item=vehicle, engine_list=engine_all, body_list=body_all, furnishing_list=furnishing_all)


def delete():
    ''' the controller for the delete page redirects views/vehicle/index.html '''

    arg_registration_no = request.args[0].replace('_', ' ')

    # new object
    obj = Vehicle.NEW()

    # check for post request
    if len(request.args) > 0:

        obj = Vehicle(request.args[0], arg_registration_no)

        VehicleDAL.delete(db, obj)

    redirect(URL('index'))
