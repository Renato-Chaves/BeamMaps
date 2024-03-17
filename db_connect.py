import city as city

class DBConnect:
    def __init__(self):
        pass
    
    def GetAdjacent(self, currentId, visited):
        if(currentId == 0):
            return [city.city(19, 'Zerind', 75), city.city(15, 'Sibiu', 140), city.city(16, 'Timisoara', 118)]
        elif(currentId == 19):
            return [city.city(12, 'Oradea', 71)]
