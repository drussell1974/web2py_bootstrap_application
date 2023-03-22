
class Urgency:

    def __init__(self, id = 0, name = ""):
        self.id = id
        self.name = str(name)


    @staticmethod
    def NEW():
        ''' Create a new instance of *urgency* '''

        obj = Urgency()

        return obj


class UrgencyDAL:

    @staticmethod
    def get_all(db):
        ''' Get all *urgency* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL urgency_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = Urgency(row[0], row[1])

                list_of_obj.append(obj)

        return list_of_obj
