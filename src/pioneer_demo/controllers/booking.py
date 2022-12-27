# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the booking controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

from booking import Booking, BookingDAL, BookingNote, BookingNoteDAL
from vehicle import Vehicle, VehicleDAL
from staff import Staff, StaffDAL
from customer import Customer, CustomerDAL
from urgency import Urgency, UrgencyDAL
from booking_type import BookingType, BookingTypeDAL

def index():
    ''' the controller for the index page that shows views/customer/index.html '''

    response.title = "Bookings - List"

    bookings_all = BookingDAL.get_all(db)

    return dict(rows=bookings_all)


def view():
    ''' the controller for the view page that shows views/customer/view.html '''

    # set page (browser tab) title
    response.title = "Booking - View"

    booking_id = request.args[0]

    booking = Booking.NEW()

    if len(request.args) > 0:
        # fetch customer from database
        booking = BookingDAL.get_by_id(db, booking_id)

    booking_note_list = BookingNoteDAL.get_all(db, booking)
    booking.booking_notes = booking_note_list

    return dict(item=booking)


def edit():
    ''' the controller for the edit page that shows views/customer/edit.html '''

    # new object
    booking = Booking.NEW()

    # check for post request

    if len(request.vars) > 0:

        booking = Booking(id=request.vars.id, description=request.vars.description, registration_no=request.vars.registration_no)
        booking.staff = Staff(id=request.vars.staff_id)
        booking.customer = Customer(id=request.vars.customer_id)
        booking.urgency = Urgency(id=request.vars.urgency_id)
        booking.booking_type = BookingType(id=request.vars.booking_type_id)
        booking.assigned_driver = Staff(id=request.vars.assigned_driver_id)

        # save
        BookingDAL.upsert(db, booking)

        # goto booking_note/index/{booking_id} page
        redirect(URL('index'))

    # set page (browser tab) title
    response.title = "Booking - Edit"

    booking = Booking.NEW()

    if len(request.args) > 0:
        # fetch customer from database
        booking = BookingDAL.get_by_id(db, request.args[0])

    vehicle_all = VehicleDAL.get_all(db)
    staff_all = StaffDAL.get_all(db)
    customer_all = CustomerDAL.get_all(db)
    urgency_all = UrgencyDAL.get_all(db)
    booking_type_all = BookingTypeDAL.get_all(db)

    return dict(item=booking, vehicle_list=vehicle_all, staff_list=staff_all, customer_list=customer_all, urgency_list=urgency_all, booking_type_list=booking_type_all)


def delete():
    ''' the controller for the delete page that redirects views/customer/index.html '''

    # new object
    booking = Booking.NEW()

    # check for post request
    if len(request.args) > 0:

        booking = Booking(request.args[0], "", "")

        BookingDAL.delete(db, booking)

    redirect(URL('index'))
