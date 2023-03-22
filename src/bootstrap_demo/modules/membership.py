from membership_level import MembershipLevel

class Membership:

    def __init__(self, id = 0, name = ""):
        self.id = id
        self.name = str(name)
        self.level = None


    @staticmethod
    def NEW():
        ''' Create a new instance of *Membership* '''

        obj = Membership()
        obj.level = MembershipLevel.NEW()

        return obj


class MembershipDAL:

    @staticmethod
    def get_all(db):
        ''' Get all *memberships* and return list'''
        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL membership_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None and len(rows) > 0:
            for row in rows:
                # create and add object to list

                obj = Membership(row[0], row[1])
                obj.level = MembershipLevel(row[2], row[3])

                list_of_obj.append(obj)

        return list_of_obj


