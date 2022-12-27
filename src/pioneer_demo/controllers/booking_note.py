# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the booking_note controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

from booking import Booking, BookingDAL, BookingNote, BookingNoteDAL

def index():
    ''' the controller for the index page that shows views/booking_note/index.html '''

    # set page (browser tab) title
    response.title = "Booking Notes"

    # inititate object
    booking = Booking.NEW()
    booking_notes = []

    # check for arguments in the url request and redirect if empty
    if len(request.args) == 0:
        redirect(URL('index'))
    else:
        booking_id = int(request.args[0]) # first value is booking
        
        booking = BookingDAL.get_by_id(db, booking_id)

        # set page (browser tab) title with booking details
        response.title = "Booking Notes for {} ({} - {})".format(booking.id, booking.registration_no, booking.customer.id)

        booking_notes = BookingNoteDAL.get_all(db, booking)

    return dict(rows=booking_notes, booking=booking)


def view():
    ''' the controller for the view page that shows views/booking_note/view.html '''

    # set page (browser tab) title
    response.title = "Booking Note - View for Booking"

    # initiate object
    booking_note = BookingNote.NEW()

    # check for at least TWO arguments in the url request and redirect if empty
    if len(request.args) < 2:
        redirect(URL('index'))
    else:
        booking_id = request.args[0] # first value in the url is the booking
        booking_note_id = request.args[1] # second value in the url is the booking_note
        
        # fetch booking note and booking (parent) from database

        booking =  BookingDAL.get_by_id(db, booking_id)
        booking_note.booking = booking

        booking_note = BookingNoteDAL.get_by_id(db, booking_note_id, booking)

    return dict(item=booking_note, booking=booking)


def edit():
    ''' the controller for the edit page that shows views/booking_note/edit.html '''

    # set page (browser tab) title
    response.title = "Booking Note - Edit for Booking"

    # initiate object
    booking_note = BookingNote.NEW()

    if len(request.vars) > 0:
        print("booking_id:", request.vars.booking_id)
        booking_note = BookingNote(request.vars.id, note=request.vars.note)
        booking_note.booking = Booking(request.vars.booking_id, request.vars.registration_no)

        # save
        BookingNoteDAL.upsert(db, booking_note)

        # goto index page
        redirect(URL('index', args=[request.vars.booking_id]))

    # check for arguments in the url request
    if len(request.args) > 0:
        booking_id = request.args[0] # first value in the url is the booking
        booking_note_id = request.args[1] if len(request.args) > 1 else 0 # second value in the url is the booking_note

        # fetch booking note and booking (parent) from database

        booking =  BookingDAL.get_by_id(db, booking_id)
        booking_note.booking = booking

        booking_note = BookingNoteDAL.get_by_id(db, booking_note_id, booking)

    return dict(item=booking_note)


def delete():
    ''' the controller for the delete page that redirects views/booking_note/index.html '''

    # new object
    booking_note = BookingNote.NEW()
    
    # check for arguments in the url request and redirect if empty
    if len(request.args) < 1:
        redirect(URL('booking','index'))
    else:
        booking_note = BookingNote(request.args[1], "", "")
        
        BookingNoteDAL.delete(db, booking_note)

        redirect(URL('index', args=[request.args[0]]))
    