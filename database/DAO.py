from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_states():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from state s"""
            cursor.execute(query)

            for row in cursor:
                result.append(
                    State(row["id"],
                          row["Name"],
                          row["Capital"],
                          row["Lat"],
                          row["Lng"],
                          row["Area"],
                          row["Population"],
                          row["Neighbors"]))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_nodes(year, shape):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                        FROM sighting s 
                        WHERE YEAR(`datetime`) = %s
                        AND shape = %s """

            cursor.execute(query, (year, shape,))

            for row in cursor:
                result.append(Sighting(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_year():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ select distinct YEAR (`datetime`) as y
                        from sighting s """

            cursor.execute(query)

            for row in cursor:
                result.append(row["y"])
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_shape(year):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else :
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT DISTINCT shape as s
                        FROM sighting s 
                        WHERE YEAR(`datetime`) = %s
                        Order by shape """

            cursor.execute(query, (year,))

            for row in cursor:
                result.append(row["s"])
            cursor.close()
            cnx.close()

        return result

