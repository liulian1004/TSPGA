#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:35:47 2021

@author: liulian
"""
import numpy as np

class TSP():
    cityCount = 0;
    numberCityMap = {};
    cityNumberMap = {};
    distanceMatrix = None;
    startCity = ""
    def __init__(self, sample, startCity):
        self.startCity = startCity;
        self.initData();
        self.sample = sample;
        
    # read the data from txt file and put them into a Map, and 2D distance array
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
    matrix[1][0]= 7.8 represent the distance between Shanghai and Bostone is 7.8
    """
    
    def buildDistanceMatrix(self, distanceMap):
       self.distanceMatrix = np.matrix([[0]*self.cityCount for i in range(self.cityCount)], dtype = float)
       for key in distanceMap:
           temp = key.split(" ");
           x = self.cityNumberMap[temp[0]];
           y = self.cityNumberMap[temp[1]];
           self.distanceMatrix[x,y] = distanceMap[key];
           self.distanceMatrix[y,x] = distanceMap[key];
           
       print(self.distanceMatrix);
            
            
def main():
    tsp= TSP(100,'Boston');
    #tsp.run(100);

if  __name__ == '__main__':
    main()
