import city as city
import pyodbc

class DBConnect:
    def __init__(self):

        self.conn = self.DatabaseConnect()
        self.cursor = self.conn.cursor()

    def DatabaseConnect(self, driver='SQL Server', server='RENATO-PC\SQLEXPRESS', database='BeamMapsDB', username=None, password=None, trusted_connection='yes'):
        connectionString = F"DRIVER={driver};SERVER={server};DATABASE={database};UTD={username};PWD={password};TRUSTED_CONNECTION{trusted_connection}"
        return pyodbc.connect(connectionString)
    
    def GetAdjacent(self, _currentId, _visited):
        sqlQuery = """SELECT
                        c2.cd_city AS cd_destiny_city,
                        c2.nm_city AS destiny_city,
                        cr.distance
                        FROM CityRoutes cr
                        INNER JOIN City c1 ON cr.id_origin = c1.cd_city
                        INNER JOIN City c2 ON cr.id_destiny = c2.cd_city
                        where c1.cd_city = {cityId}""".format(cityId = _currentId)
        self.cursor.execute(sqlQuery)
        queryFetch = self.cursor.execute(sqlQuery).fetchall()
        self.adjacents = []

        for adjacent in queryFetch:
            if(not (adjacent[0] in _visited)):
                self.adjacents.append(city.city(adjacent[0], adjacent[1], adjacent[2]))
        
        return self.adjacents

            
        # if(_currentId == 0):
        #     return [city.city(19, 'Zerind', 75), city.city(15, 'Sibiu', 140), city.city(16, 'Timisoara', 118)]
        # elif(_currentId == 19):
        #     return [city.city(12, 'Oradea', 71)]

    def GetCityName(self, _cityId):
        sqlQuery = ("select nm_city from City where cd_city = {cityId}".format(cityId = _cityId))
        self.cursor.execute(sqlQuery)
        return str(self.cursor.fetchall()[0][0])