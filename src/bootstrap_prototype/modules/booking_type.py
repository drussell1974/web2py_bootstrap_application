
class BookingType:

    def __init__(self, id = 0, name = ""):
        self.id = id
        self.name = str(name)


    @staticmethod
    def NEW():
        ''' Create a new instance of *booking_type* '''

        obj = BookingType()

        return obj


class BookingTypeDAL:

    @staticmethod
    def get_all(db):
        ''' Get all *booking_type* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL call_type_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = BookingType(row[0], row[1])

                list_of_obj.append(obj)

        return list_of_obj
