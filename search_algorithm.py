import db_connect as db
import sorting_vector as sort
import numpy as np

class Greedy:             #Searching Class
    def __init__(self, objective):
        self.objective = objective
        self.found = False   #Indicates if objective was found
        self.visited = []
        self.dbConnection = db.DBConnect()
        self.resultTxt = ""
        self.resultDist = 0
        self.roadPath0 = []
        self.roadPath1 = []


    def search(self, current):
        print('-------')
        print('current: ', current.name)
        self.visited.append(current.id)

        if(current.id == self.objective):
            self.found = True
            # self.resultTxt += ("----------\nYou've reached your objective")
            print("You've reached your objective")
        else: 
            for adjacent in self.dbConnection.GetAdjacent(current.id, self.visited):
                # self.resultTxt += ("\n"+str(adjacent.id)+" - "+str(adjacent.name)+" - "+str(adjacent.dist))
                # self.resultTxt += ("\n", adjacent.id, " - ", adjacent.name, " - ", adjacent.dist)
                print(adjacent.id," - ", adjacent.name, " - ", adjacent.dist)
            adjacents = self.dbConnection.GetAdjacent(current.id, self.visited)
            self.sortedVector = sort.SortedVector(len(adjacents))
            self.sortedVector.sortAdjacents(adjacents)
            if(len(self.sortedVector.values)>0):
                self.resultTxt += current.name+" -> "+self.sortedVector.values[0].name+"\n"+str(self.sortedVector.values[0].dist)+"km\n"
                self.roadPath0.append(current.id)
                self.roadPath1.append(self.sortedVector.values[0].id)
                self.resultDist += self.sortedVector.values[0].dist
            else:
                self.resultTxt = "Route not Found"

            if(len(self.sortedVector.values)>0):
                self.search(self.sortedVector.values[0])