
class Body:

    def __init__(self, id = 0, name = ""):
        self.id = id
        self.name = str(name)
        self.vehicle = None


    @staticmethod
    def NEW(id = 0):
        ''' Create a new instance of *body* '''

        obj = Body(id)

        return obj


class BodyDAL:

    @staticmethod
    def get_all(db):
        ''' Get all *body* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL body_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = Body(row[0], row[1])

                list_of_obj.append(obj)

        return list_of_obj


    def get_for_vehicle(db, vehicle):
        ''' Get *body* by vehicle.id and return object'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL vehicle_body_get('{}');".format(vehicle.id)
        rows = db.executesql(qry)

        # prepare results

        for row in rows:
            # create object

            obj = Body(row[0], row[1])
            list_of_obj.append(obj)
            
        return list_of_obj


    def insert_for_vehicle(db, vehicle):
        ''' Insert *body* by vehicle (deletes then reinserts)'''

        qry2 = 'CALL vehicle_body_delete("{}");'.format(vehicle.registration_no)
        db.executesql(qry2)
        
        for x in vehicle.body:
            qry3 = 'CALL vehicle_body_insert({}, "{}");'.format(x.id, vehicle.registration_no)
            db.executesql(qry3)
        
        # do nothing
        pass