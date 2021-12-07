#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:35:47 2021

@author: liulian
"""
import numpy as np
from GA import GA
import random

class TSP(object):
    cityCount = 0;
    numberCityMap = {};
    cityNumberMap = {};
    distanceMatrix = None;
    startCity = "";
    crossoverRate = 0.6;
    mutationRate = 0.001;
    
    def __init__(self, sample, cities, startCity):
        self.startCity = startCity;
        self.sample = sample;
        self.cityCount = cities;
        #self.initData();
        self.initRandomData();
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
    create my own data with 10 cities
    the distances is randomly generate from  10 to 100;
    ex:
    
   [[64.45674898 68.97780026 80.36714622 81.75647249 22.53456572 86.86040092
  42.40720899 99.47232777 19.18298575 55.7402768 ]
 [12.83397604 22.06168876 22.54496506 25.64414999 75.19166113 35.27284311
  94.75366705 86.93304205 97.77456322 67.88698807]
 [18.00160779 84.98450145 91.16537275 78.7325785  20.25498235 93.48084496
  37.57708027 51.54719276 68.82018587 45.31268902]
 [76.23337022 40.95333253 41.75587335 32.73040736 78.67935498 76.04214342
  17.98006804 77.7251739  12.69403123 15.59720479]
 [73.52649703 77.32457041 60.4727587  78.53570622 12.16061295 32.89881415
  58.95602481 35.73464804 51.089779   31.245628  ]
 [13.57191018 55.78858281 99.4538467  22.46674932 60.67535841 19.96086445
  56.09961255 98.38942045 47.35893505 27.59901955]
 [43.30186665 46.68372886 64.25027648 93.86382716 77.62948235 18.28511797
  61.11050434 18.72044412 92.83046168 33.14221651]
 [55.30195851 51.88451202 53.28785882 34.39666155 52.67905538 76.2477322
  78.47866361 53.56970402 67.34155197 84.75026291]
 [68.09594238 38.61557516 95.04047016 45.24321363 95.77234222 93.13066674
  99.24889186 61.64602887 24.34798968 67.12550072]
 [55.83721858 47.38263952 23.11906123 95.88255061 80.07087839 21.44917072
  22.38536848 14.09780128 76.84448038 42.0454291 ]] 
    """
    def initRandomData(self):
        self.distanceMatrix = np.matrix([[0]*self.cityCount for i in range(self.cityCount)], dtype = float)
        for i in range(self.cityCount):
            for j in range(self.cityCount):
                self.distanceMatrix[i,j] = random.uniform(10.00, 100.00);

    """
    run the GA with professor defined data
    
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
    
    
            
    """
    run the GA with times and self denfined data
    
    """
    def runSelfData(self, times):
        while times > 0:
            self.ga.nextGeneration();
            best = self.ga.best
            print("best route is")
            print(best.route)
            print("with %f"%(best.distance))
            times -= 1;
    
            
def main():
    samples = 100;
    cities = 10;
    tsp= TSP(samples,cities,'Boston');
    tsp.runSelfData(10)
    #tsp.run(10);

if  __name__ == '__main__':
    main()
