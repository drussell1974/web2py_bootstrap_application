# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is the booking_note controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

from booking import Booking, BookingDAL, BookingNote, BookingNoteDAL

def index():
    ''' the controller for the index page that shows views/booking_note/index.html '''

    booking_id = int(request.args[0]) # first value is booking
    booking = Booking.NEW()
    booking = BookingDAL.get_by_id(db, booking_id)

    response.title = "Booking Notes for {}".format(booking_id)

    booking_notes = BookingNoteDAL.get_all(db, booking)

    return dict(rows=booking_notes, booking=booking)


def view():
    ''' the controller for the view page that shows views/booking_note/view.html '''

    booking_id = request.args[0] # first value in the url is the booking
    booking_note_id = request.args[1] if len(request.args) > 1 else 0 # second value in the url is the booking_note

    # set page (browser tab) title
    response.title = "Booking Note - View for Booking {}".format(booking_id)

    # fetch booking note and booking (parent) from database

    booking_note = BookingNote.NEW()

    booking =  BookingDAL.get_by_id(db, booking)
    booking_note.booking = booking

    booking_note = BookingNoteDAL.get_by_id(db, booking_note_id, booking)

    return dict(item=booking_note, booking=booking)




def edit():
    ''' the controller for the edit page that shows views/booking_note/edit.html '''

    booking_id = request.args[0] # first value in the url is the booking
    booking_note_id = request.args[1] if len(request.args) > 1 else 0 # second value in the url is the booking_note

    if len(request.vars) > 0:

        booking_note = BookingNote(request.vars.id, note=request.vars.note)
        booking_note.booking = Booking(request.vars.booking_id, request.vars.registration_no)

        # save
        BookingNoteDAL.upsert(db, booking_note)

        # goto index page
        redirect(URL('index', args=[booking_id]))

    # show page

    response.title = "Booking Note - Edit for Booking {}".format(booking_id)

    # fetch booking note and booking (parent) from database

    booking_note = BookingNote.NEW()

    booking =  BookingDAL.get_by_id(db, booking_id)
    booking_note.booking = booking

    booking_note = BookingNoteDAL.get_by_id(db, booking_note_id, booking)

    return dict(item=booking_note, booking=booking)


def delete():
    ''' the controller for the delete page that redirects views/booking_note/index.html '''

    # new object
    booking_note = BookingNote.NEW()
    booking_note.booking.id = int(request.args[1])

    # check for post request
    if len(request.args) > 0:

        booking_note = BookingNote(request.args[1], "", "")

        BookingNoteDAL.delete(db, booking_note)

    redirect(URL('index', args=[request.args[0]]))
