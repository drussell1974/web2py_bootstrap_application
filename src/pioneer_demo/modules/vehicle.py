from engine import Engine, EngineDAL
from body import Body, BodyDAL
from furnishing import Furnishing, FurnishingDAL

class Vehicle:

    def __init__(self, id = "", registration_no = ""):
        self.id = str(id) # for storing the old registration no if changed
        self.registration_no = str(registration_no)
        self.engine = []
        self.body = []
        self.furnishing = []


    @staticmethod
    def NEW():
        ''' Create a new instance of *vehicle* '''

        obj = Vehicle()

        return obj


class VehicleDAL:

    @staticmethod
    def get_by_id(db, id):
        ''' Get *vehicle* by id and return object'''

        obj = Vehicle.NEW()
        rows = []

        # execute statement and fetch data

        qry = "CALL vehicle_get_byid('{}');".format(id)
        rows = db.executesql(qry)

        # prepare results

        if rows is not None and len(rows) > 0:
            # create object

            obj = Vehicle(rows[0][0], rows[0][0])
            
        return obj


    @staticmethod
    def get_all(db):
        ''' Get all *vehicle* and return list'''

        list_of_obj = []
        rows = []

        # execute statement and fetch data

        qry = "CALL vehicle_get_all();"
        rows = db.executesql(qry)

        # prepare results

        if rows is not None or len(rows) > 0:
            # create and add object to list
            for row in rows:
                obj = Vehicle(row[0], row[0])

                list_of_obj.append(obj)

        return list_of_obj


    @staticmethod
    def upsert(db, vehicle):
        ''' Update or Insert *vehicle* '''

        qry1 = 'CALL vehicle_upsert("{}", "{}");'.format(vehicle.id, vehicle.registration_no)
        db.executesql(qry1)
            
        # do nothing
        pass


    @staticmethod
    def delete(db, vehicle):
        ''' Delete *vehicle* '''

        # execute statement

        qry = 'CALL vehicle_delete("{}");'.format(vehicle.registration_no)
        db.executesql(qry)

        # do nothing
        pass
