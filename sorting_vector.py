import numpy as np
import city as city

class SortedVector():
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=object)

    def sortAdjacents(self, adjacents):
        self.values = sorted(adjacents, key=lambda x: x.dist)

        # for adjacent in adjacents:
        #     if(dist == -1):
        #         dist = adjacent.dist
        #         self.nearestCity = adjacent
        #     elif(dist > adjacent.dist):
        #         dist = adjacent.dist
        #         self.nearestCity = adjacent
        #     index += 1
