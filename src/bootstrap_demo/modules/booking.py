from staff import Staff, StaffDAL
from customer import Customer, CustomerDAL
from urgency import Urgency, UrgencyDAL
from booking_type import BookingType, BookingTypeDAL

class Booking:

    def __init__(self, id = 0, time_of_call = "", description = "", registration_no = ""):
        self.id = id
        self.time_of_call = time_of_call
        self.description = str(description)
        self.registration_no = str(registration_no)
        self.staff = Staff.NEW()
        self.customer = Customer.NEW()
        self.urgency = Urgency.NEW()
        self.booking_type = BookingType.NEW()
        self.assigned_driver = Staff.NEW()
        self.booking_notes = []


    @staticmethod
    def NEW():
        ''' Create a new instance of *Booking* '''

        obj = Booking()

        return obj


class BookingDAL:

    @staticmethod
    def get_by_id(db, booking_id):
        ''' Get *Booking* by id and return object'''

        booking = Booking.NEW()
        rows = []

        # execute statement and fetch data

        qry = "CALL booking_get_byid({});".format(booking_id)

        rows = db.executesql(qry)

        # prepare results

        if rows is not None and len(rows) > 0:
            # create object
            # NOTE: rows[0] is the first row
            # NOTE: rows[0][0] and rows[0][1] are the first column and second column respectively
            booking = Booking(id=rows[0][0], time_of_call=rows[0][1], description=rows[0][2], registration_no=rows[0][3])
            booking.staff = Staff(id=rows[0][4], first_name=rows[0][5], surname=rows[0][6])
            booking.customer = Customer(id=rows[0][7], first_name=rows[0][8], surname=rows[0][9])
            booking.urgency = Urgency(id=rows[0][10], name=rows[0][11])
            booking.booking_type = BookingType(id=rows[0][12], name=rows[0][13])
            booking.assigned_driver = Staff(id=rows[0][14], first_name=rows[0][15], surname=rows[0][16])

        return booking


    @staticmethod
    def get_all(db):
        ''' Get all *Booking* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL booking_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                booking = Booking(id=row[0], time_of_call=row[1], description=row[2], registration_no=row[3])
                booking.staff = Staff(id=row[4], first_name=row[5], surname=row[6])
                booking.customer = Customer(id=row[7], first_name=row[8], surname=row[9])
                booking.urgency = Urgency(id=row[10], name=row[11])
                booking.booking_type = BookingType(id=row[12], name=row[13])
                booking.assigned_driver = Staff(id=row[14], first_name=row[15], surname=row[16])

                list_of_obj.append(booking)

        return list_of_obj


    @staticmethod
    def upsert(db, booking):
        ''' Update or Insert *Booking* '''

        # execute statement

        qry = 'CALL booking_upsert({}, "{}", "{}", {}, {}, {}, {}, {})'.format(booking.id, booking.description, booking.registration_no, booking.staff.id, booking.customer.id, booking.urgency.id, booking.booking_type.id, booking.assigned_driver.id)
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
            obj.booking = booking

        return obj


    @staticmethod
    def get_all(db, booking):
        ''' Get all *BookingNote* and return list'''

        list_of_obj = []
        rows = []

        # execute statement

        qry = "CALL booking_note_get_all({});".format(booking.id)
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = BookingNote(row[0], row[1], row[2])
                obj.booking = booking

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

