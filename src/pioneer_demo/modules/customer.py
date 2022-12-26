from membership import Membership
from membership_level import MembershipLevel

class Customer:

    def __init__(self, id = 0, first_name = "", surname = ""):
        self.id = id
        self.first_name = str(first_name)
        self.surname = str(surname)
        self.membership = None


    @staticmethod
    def NEW():
        ''' Create a new instance of *Customer* '''

        obj = Customer()
        obj.membership = Membership.NEW()

        return obj


class CustomerDAL:

    @staticmethod
    def get_by_id(db, id):
        ''' Get *Customer* by id and return object'''

        obj = None
        rows = []

        # execute statement to fetch data

        qry = "CALL customer_get_byid({});".format(id)
        rows = db.executesql(qry)

        # prepare results

        if rows is not None and len(rows) > 0:
            # create object

            obj = Customer(rows[0][0], rows[0][1], rows[0][2])
            obj.membership = Membership(rows[0][3], rows[0][4])
            obj.membership.level = MembershipLevel(rows[0][5], rows[0][6])

        return obj


    @staticmethod
    def get_all(db):
        ''' Get all *Customers* and return list'''

        list_of_obj = []
        rows = []

        # execute statement to fetch results

        qry = "CALL customer_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = Customer(row[0], row[1], row[2])
                obj.membership = Membership(row[3], row[4])
                obj.membership.level = MembershipLevel(row[5], row[6])

                list_of_obj.append(obj)

        return list_of_obj


    @staticmethod
    def upsert(db, customer):
        ''' Update or Insert *Customer* '''

        # execute statement

        qry = 'CALL customer_upsert({}, "{}", "{}", {})'.format(customer.id, customer.first_name, customer.surname, customer.membership.id)
        db.executesql(qry)

        # do nothing
        pass


    @staticmethod
    def delete(db, customer):
        ''' Delete *Customer* '''

        qry = 'CALL customer_delete({})'.format(customer.id)
        db.executesql(qry)

        # do nothing
        pass
