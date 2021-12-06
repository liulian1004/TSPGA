#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:35:47 2021

@author: liulian
"""
import numpy as np
from GA import GA

class TSP(object):
    cityCount = 0;
    numberCityMap = {};
    cityNumberMap = {};
    distanceMatrix = None;
    startCity = "";
    crossoverRate = 0.6;
    mutationRate = 0.001;
    def __init__(self, sample, startCity):
        self.startCity = startCity;
        self.initData();
        self.sample = sample;
        self.ga = GA(self.cityCount,self.sample, self.distanceMatrix)
        
    # read the data from txt file and process the data
    def initData(self):
        cities = set();
        distanceMap = {};
        f = open('datasource.txt', 'r');
        lines = f.readlines();
        f.close();
        for line in lines:
            #read the line one by one, collection the cities set;
            line = line.split(" ");
            cities.add(line[0]);
            cities.add(line[1]);
            key = line[0] + " " + line[1];
            value = float(line[2].replace("\n",""));
            distanceMap.update({key:value});
        
        self.cityCount = len(cities);
        self.buildCityMap(cities);
        self.buildDistanceMatrix(distanceMap);
        
  
    """
       build the map with number and city  
       0 for start city, the rest is sort by letter
       ex: numberCityMap: {0: 'Boston', 1: 'Shanghai', 2: 'Mumbai', 3: 'London'}
    """
    def buildCityMap(self, cities):
        self.numberCityMap.update({0:self.startCity});
        self.cityNumberMap.update({self.startCity:0});
        cities.remove(self.startCity);
        sorted(cities);
        startIndex = 1;
        for city in cities:
            self.numberCityMap.update({startIndex: city});
            self.cityNumberMap.update({city:startIndex});
            startIndex += 1;
            
    
    """
    buid the 2D float matrix to represent the distance
    ex:  [ [0.  7.8 7.6 3. ]
         [7.8 0.  3.1 5.7]
         [7.6 3.1 0.  4.5]
         [3.  5.7 4.5 0. ]]
    {0: 'Boston', 1: 'Shanghai', 2: 'Mumbai', 3: 'London'}
    matrix[1][0]= 7.8 represent the distance between Shanghai and Boston is 7.8
    """
    
    def buildDistanceMatrix(self, distanceMap):
       self.distanceMatrix = np.matrix([[0]*self.cityCount for i in range(self.cityCount)], dtype = float)
       for key in distanceMap:
           temp = key.split(" ");
           x = self.cityNumberMap[temp[0]];
           y = self.cityNumberMap[temp[1]];
           self.distanceMatrix[x,y] = distanceMap[key];
           self.distanceMatrix[y,x] = distanceMap[key];
    
    
    """
    run the GA with times
    
    
    def initRandomData(self):
    """
    
    """
    run the GA with times
    
    """
    def run(self, times):
        while times > 0:
            self.ga.nextGeneration();
            best = self.ga.best
            route = [];
            for city in best.route:
                route.append(self.numberCityMap[city])
            print("best route is")
            print(route)
            print("with %f"%(best.distance))
            times -= 1;
            
    
    def evulationFuntion(self, life):
        distance = 0.0
        for i in range(0, len(life)-2):
            index1, index2 = life[i], life[i+1]
            distance += self.distanceMatrix[index1,index2];
        print(distance)
        return 1/distance;
            
def main():
    tsp= TSP(3,'Boston');
    #print(tsp.evulationFuntion([0,1,2,3,0]))
    #print(tsp.evulationFuntion([0, 3, 2, 1, 0]))
    tsp.run(10);

if  __name__ == '__main__':
    main()
