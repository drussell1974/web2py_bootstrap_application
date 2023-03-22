
class Engine:

    def __init__(self, id = 0, name = ""):
        self.id = id
        self.name = str(name)
        self.vehicle = None


    @staticmethod
    def NEW(id = 0):
        ''' Create a new insta nce of *engine* '''

        obj = Engine(id)

        return obj


class EngineDAL:

    @staticmethod
    def get_all(db):
        ''' Get all *engine* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL engine_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = Engine(row[0], row[1])

                list_of_obj.append(obj)

        return list_of_obj


    @staticmethod
    def get_for_vehicle(db, vehicle):
        ''' Get *engine* by vehicle.id and return object'''

        list_of_obj = []
        rows = []


        # execute statement and fetch data

        qry = "CALL vehicle_engine_get('{}');".format(vehicle.id)
        rows = db.executesql(qry)

        # prepare results

        for row in rows:
            # create object

            obj = Engine(row[0], row[1])
            obj.vehicle = vehicle

            list_of_obj.append(obj)
            
        return list_of_obj


    def insert_for_vehicle(db, vehicle):
        ''' Insert *engine* by vehicle (deletes then reinserts)'''

        qry_delete = 'CALL vehicle_engine_delete("{}");'.format(vehicle.registration_no)
        db.executesql(qry_delete)
        
        for x in vehicle.engine:
            qry_insert = 'CALL vehicle_engine_insert({}, "{}");'.format(x.id, vehicle.registration_no)
            db.executesql(qry_insert)
        
        # do nothing
        pass