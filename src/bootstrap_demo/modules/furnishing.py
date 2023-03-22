
class Furnishing:

    def __init__(self, id = 0, name = ""):
        self.id = id
        self.name = str(name)
        self.vehicle = None


    @staticmethod
    def NEW(id = 0):
        ''' Create a new instance of *furnishing* '''

        obj = Furnishing(id)

        return obj


class FurnishingDAL:

    @staticmethod
    def get_all(db):
        ''' Get all *furnishing* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL furnishing_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = Furnishing(row[0], row[1])

                list_of_obj.append(obj)

        return list_of_obj


    def get_for_vehicle(db, vehicle):
        ''' Get *furnishing* by vehicle.id and return object'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL vehicle_furnishing_get('{}');".format(vehicle.id)
        rows = db.executesql(qry)

        # prepare results

        for row in rows:
            # create object

            obj = Furnishing(row[0], row[1])
            list_of_obj.append(obj)
            
        return list_of_obj


    def insert_for_vehicle(db, vehicle):
        ''' Insert *furnishing* by vehicle (deletes then reinserts)'''

        qry_delete = 'CALL vehicle_furnishing_delete("{}");'.format(vehicle.registration_no)
        db.executesql(qry_delete)
        
        for x in vehicle.furnishing:
            qry_insert= 'CALL vehicle_furnishing_insert({}, "{}");'.format(x.id, vehicle.registration_no)
            db.executesql(qry_insert)
        
        # do nothing
        pass
