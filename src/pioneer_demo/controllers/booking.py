# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the booking controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

from booking import Booking, BookingDAL
from vehicle import Vehicle, VehicleDAL
from staff import Staff, StaffDAL
from customer import Customer, CustomerDAL
from urgency import Urgency, UrgencyDAL
from booking_type import BookingType, BookingTypeDAL

def index():
    ''' the controller for the index page that shows views/customer/index.html '''

    response.title = "Bookings - List"

    booking_rows = BookingDAL.get_all(db)

    return dict(rows=booking_rows)


def view():
    ''' the controller for the view page that shows views/customer/view.html '''

    # set page (browser tab) title
    response.title = "Booking - View"

    booking = Booking.NEW()

    if len(request.args) > 0:
        # fetch customer from database

        booking = BookingDAL.get_by_id(db, request.args[0])
        # TODO: Get One-to-Many

    #memberships = MembershipDAL.get_all(db)

    return dict(item=booking)


def edit():
    ''' the controller for the edit page that shows views/customer/edit.html '''

    # new object
    booking = Booking.NEW()

    # check for post request

    if len(request.vars) > 0:

        booking = Booking(id=request.vars.id, description=request.vars.description, registration_no=request.vars.registration_no)
        #customer.membership = Membership(request.vars.membership_id)

        # save
        BookingDAL.upsert(db, booking)

        # goto index page
        redirect(URL('index'))

    # set page (browser tab) title
    response.title = "Booking - Edit"

    booking = Booking.NEW()

    if len(request.args) > 0:
        # fetch customer from database
        booking = BookingDAL.get_by_id(db, request.args[0])

    vehicles = VehicleDAL.get_all(db)
    staff = StaffDAL.get_all(db)
    customers = CustomerDAL.get_all(db)
    urgencies = UrgencyDAL.get_all(db)
    booking_types = BookingTypeDAL.get_all(db)

    return dict(item=booking, vehicle_list=vehicles, staff_list=staff, customer_list=customers, urgency_list=urgencies, booking_type_list=booking_types)


def delete():
    ''' the controller for the delete page that redirects views/customer/index.html '''

    # new object
    customer = Customer.NEW()

    # check for post request
    if len(request.args) > 0:

        customer = Customer(request.args[0], "", "")

        CustomerDAL.delete(db, customer)

    redirect(URL('index'))
