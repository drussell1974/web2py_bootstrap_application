
class MembershipLevel:

    def __init__(self, id = 0, name = ""):
        self.id = id
        self.name = str(name)


    @staticmethod
    def NEW():
        ''' Create a new instance of *MembershipLevel* '''

        obj = MembershipLevel()

        return obj


class MembershipLevelDAL:

    @staticmethod
    def get_by_id(db, id):
        ''' Get *membership level* by id and return object '''

        obj = MembershipLevel.NEW()
        rows = []

        # execute statement and fetch data

        qry = "CALL membershiplevel_get_byid({});".format(id)
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            obj.id = int(rows[0])
            obj.name = str(rows[1])

        return obj


    @staticmethod
    def get_all(db):
        ''' Get all *membership levels* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL membershiplevel_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list

            obj = MembershipLevel(rows[0], rows[1])

            list_of_obj.append(obj)

        return list_of_obj
