
class Booking:

    def __init__(self, id = 0, time_of_call = "", description = "", registration_no = "", booking_notes = []):
        self.id = id
        self.time_of_call = time_of_call
        self.description = str(description)
        self.registration_no = str(registration_no)
        self.booking_notes = booking_notes


    @staticmethod
    def NEW():
        ''' Create a new instance of *Booking* '''

        obj = Booking()

        return obj


class BookingNote:

    def __init__(self, id = 0, date = "", note = ""):
        self.id = id
        self.date = date
        self.note = str(note)
        self.booking = None


    @staticmethod
    def NEW():
        ''' Create a new instance of *BookingNote* '''

        obj = BookingNote()
        obj.booking = Booking.NEW()

        return obj


class BookingDAL:

    @staticmethod
    def get_by_id(db, id):
        ''' Get *Booking* by id and return object'''

        booking = Booking.NEW()
        rows = []

        # execute statement and fetch data

        qry = "CALL booking_get_byid({});".format(id)

        rows = db.executesql(qry)

        # DEBUG: DEVELOPMENT ONLY
        #raise Exception("qry:{}, rows:{}".format(qry, rows))

        # prepare results

        if rows is not None and len(rows) > 0:
            # create object

            booking = Booking(rows[0][0], rows[0][1], rows[0][2], rows[0][3])

            # TODO: Get notes

        # DEBUG: DEVELOPMENT ONLY
        #raise Exception("id:{}, time:{}, description:{}, reg_no:{}".format(booking.id, booking.time_of_call, booking.description, booking.registration_no))

        return booking


    @staticmethod
    def get_all(db, id):
        ''' Get all *Booking* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL booking_get_all({});".format(booking_id)
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                booking = Booking(rows[0][0], rows[0][1], rows[0][2], registration_no=rows[0][3])
                list_of_obj.append(booking)

        return list_of_obj


    @staticmethod
    def upsert(db, booking):
        ''' Update or Insert *Booking* '''

        # execute statement

        qry = 'CALL booking_upsert({}, "{}", "{}")'.format(booking.id, booking.description, booking.registration_no)
        db.executesql(qry)

        # do nothing
        pass


    @staticmethod
    def delete(db, booking):
        ''' Delete *Booking* '''

        # execute statement

        qry = 'CALL booking_delete({})'.format(booking.id)
        db.executesql(qry)

        # do nothing
        pass

class BookingNoteDAL:

    @staticmethod
    def get_by_id(db, id, booking):
        ''' Get *Booking* by id and return object'''

        obj = BookingNote.NEW()
        obj.booking = booking
        rows = []

        # execute statement and fetch data

        qry = "CALL booking_note_get_byid({});".format(id)

        rows = db.executesql(qry)

        # prepare results

        if rows is not None and len(rows) > 0:
            # create object

            obj = BookingNote(rows[0][0], rows[0][1], rows[0][2])
            obj.booking = Booking(rows[0][3], rows[0][4], rows[0][5], rows[0][6])

        return obj


    @staticmethod
    def get_all(db, booking_id):
        ''' Get all *BookingNote* and return list'''

        list_of_obj = []
        rows = []


        # execute statement

        qry = "CALL booking_note_get_all({});".format(booking_id)
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = BookingNote(row[0], row[1], row[2])
                obj.booking = Booking(rows[0][3], rows[0][4], rows[0][5], rows[0][6])

                list_of_obj.append(obj)

        return list_of_obj


    @staticmethod
    def upsert(db, booking_note):
        ''' Update or Insert *BookingNote* '''

        # execute statement

        qry = 'CALL booking_note_upsert({}, "{}", {})'.format(booking_note.id, booking_note.note, booking_note.booking.id)
        db.executesql(qry)

        # do nothing
        pass


    @staticmethod
    def delete(db, customer):
        ''' Delete *BookingNote* '''

        # execute statement

        qry = 'CALL booking_note_delete({})'.format(customer.id)
        db.executesql(qry)

        # do nothing
        pass

