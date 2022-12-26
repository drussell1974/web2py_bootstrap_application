
class Staff:

    def __init__(self, id = 0, first_name = "", surname = ""):
        self.id = id
        self.first_name = str(first_name)
        self.surname = str(surname)


    @staticmethod
    def NEW():
        ''' Create a new instance of *staff* '''

        obj = Staff()

        return obj

    @property
    def full_name():
        return "{}, {}".format(self.surname, self.first_name)


class StaffDAL:

    @staticmethod
    def get_all(db):
        ''' Get all *urgency* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL staff_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = Staff(row[0], row[1], row[2])

                list_of_obj.append(obj)

        return list_of_obj
