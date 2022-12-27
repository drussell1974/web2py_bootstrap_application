# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the customer controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

from customer import Customer, CustomerDAL
from membership import Membership, MembershipDAL
from membership_level import MembershipLevel, MembershipLevelDAL


def index():
    ''' the controller for the index page that shows views/customer/index.html '''

    response.title = "Customers - List"

    customer_rows = CustomerDAL.get_all(db)

    return dict(rows=customer_rows)


def view():
    ''' the controller for the view page that shows views/customer/view.html '''

    # set page (browser tab) title
    response.title = "Customer - View"

    # initiate object
    customer = Customer.NEW()

    # check for arguments in the url request and redirect if empty
    if len(request.args) == 0:
        redirect(URL('index'))
    else:
        customer = CustomerDAL.get_by_id(db, request.args[0])

        memberships = MembershipDAL.get_all(db)

    return dict(item=customer)


def edit():
    ''' the controller for the edit page that shows views/customer/edit.html '''

    # set page (browser tab) title
    response.title = "Customer - Edit"

    # initiate object
    customer = Customer.NEW()

    # check for post request
    if len(request.vars) > 0:

        customer = Customer(request.vars.id, request.vars.first_name, request.vars.surname)
        customer.membership = Membership(request.vars.membership_id)

        # save
        CustomerDAL.upsert(db, customer)

        # goto index page
        redirect(URL('index'))

    # check for arguments in the url request
    if len(request.args) > 0:
        # fetch customer from database

        customer = CustomerDAL.get_by_id(db, request.args[0])

    membership_all = MembershipDAL.get_all(db)

    return dict(item=customer, memberships=membership_all)


def delete():
    ''' the controller for the delete page that redirects views/customer/index.html '''

    # initiate object
    customer = Customer.NEW()

    # check for arguments in the url request and redirect if empty
    if len(request.args) == 0:
        redirect(URL('index'))
    else:
        customer = Customer(request.args[0], "", "")

        CustomerDAL.delete(db, customer)

    redirect(URL('index'))
