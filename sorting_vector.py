import numpy as np
import city as city

class SortedVector():
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.nearestCity = city.city(0, "")
        # change in data type
        self.values = np.empty(self.capacity, dtype=object)

    def sortAdjacents(self, adjacents):
        dist = -1
        for adjacent in adjacents:
            if(dist == -1):
                dist = adjacent.dist
                self.nearestCity = adjacent
            elif(dist > adjacent.dist):
                dist = adjacent.dist
                self.nearestCity = adjacent
