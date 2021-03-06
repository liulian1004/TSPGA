#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:14:44 2021

@author: liulian
"""
import random


from LIFE import Life

class GA(object):
    population = [];
    counts = 0;
    best = None;
    evulationFuntion = None;
    distanceMatrix = None;
    crossoverRate = 0.6;
    mutationRate = 0.001;

    
    def __init__(self, counts, samples, distanceMatrix):
        self.counts = counts;
        self.samples = samples;
        self.distanceMatrix = distanceMatrix;
        self.initPopulation();
        
    
    
    """  
    generate the sample number of random path, the number of sample passed by TSP_main
    ex: one of random path for 4 cities and start and end at city 0
    [0,1,2,3,0]
    """
    def initPopulation(self):
        self.population = [];
        
        for i in range(self.samples):
            # here shall exclude the start city, which I will append manually
            cities = list(range(self.counts-1));
            random.shuffle(cities);
            route = [];
            route.append(0);
            for number in cities:
                number += 1;
                route.append(number);
            route.append(0);
            life = Life(route);
            self.population.append(life);
        
        
        
    """  
    generate the index random, and copy the parent2[index, parent2.length-1] as the part of child
    ex: 
    index = 2;
    p1 = [0,1,2,3,0]; 
    p2 = [0,2,3,1,0]; 
    child = [0,3,1,2,0]
    """
    def crossOver(self, parent1, parent2):
        # the index shall start from 1, and exclude the end and start index, which represent start city
        index = random.randint(1, self.counts-2);
        # this is the part which shall copy from parent2
        copyPart = parent2.route[index: len(parent2.route)-1];
        child = [];
        #child start with start city
        child.append(0);
        # P1 is the point pointer to the 1 index of parent1
        p1 = 1;
        for city in parent1.route:
            if city == 0:
                continue;
            if p1 == index:
                child.extend(copyPart)
            if city not in copyPart:
                child.append(city)
            p1 += 1;
        # child shall end at start city
        child.append(0);
        return Life(child);
    
    
    """  
    generate two index randomly between 1 and child.length-1, and swap
    ex: 
    before mutation: [0,1,2,3,0]
    after mutation: [0,1,3,2,0]
    """
    def mutation(self, child):
         index1 = random.randint(1, len(child.route)-2);
         index2 = random.randint(1, len(child.route)-2);
         child.route[index1], child.route[index2] = child.route[index2],child.route[index1];
         return child;
    
    
    """
    the calculateRate return the 1/distance;
    and the distance is the sum of distance based on the order of route
    since we look for the smallest sum, so the eveluationFunction shall return 1/sum
    which represent the biggest result of evulationFuntion
    
    """
    def calculateRate(self, life):
        distance = 0.0
        for i in range(0, len(life.route)-1):
            index1, index2 = life.route[i], life.route[i+1]
            distance += self.distanceMatrix[index1,index2];
            
        life.distance = distance;
        return 1/distance;
    
    
    """
    the evalutaion function is to compare the rate of smaples, and return the best rate sample
    which will call calcuateRate function to calcalute the rate of each route
    """
    
    def evaluation(self):
        #init the first route is the best and calcuate its score
        self.best = self.population[0];
        self.best.rate = self.calculateRate(self.best);
        for life in self.population:
            life.rate = self.calculateRate(life);
            # upate the best route if the cur one is better
            if self.best.rate < life.rate:
                self.best = life;

    
    """ 
    pickUpParent is to ramdomly pickup one sample as the parent
    """ 
    def pickUpParent(self):
        index = random.randint(0, self.samples-1);
        return self.population[index];
    
    """ 
    generateChild is to generate the  child. Here I generate a random figure.
    if the random < crossover Rate or < mutation Rate, it will trigger these function
    
    """ 
    def generateChild(self):
        parent1 = self.pickUpParent();
        rate1 = random.uniform(0, 1);
        if rate1 < self.crossoverRate:
            parent2 = self.pickUpParent();
            child = self.crossOver(parent1, parent2);
        else:
            child = parent1;
            
        rate2 = random.uniform(0, 1);
        if rate2 < self.mutationRate:
            self.mutation(child);
        return child;
    
    """ 
    nextGeneratetion is for generate the next population
    first of all, I will put the best route into the next generation
    and the result of popluation will be generate by the generateChild function
    
    """ 
    def nextGeneration(self):
        #find the best route in this poupluation
        self.evaluation();
        nextPopuluation = [];
        nextPopuluation.append(self.best);
        while len(nextPopuluation) < self.samples:
            nextPopuluation.append(self.generateChild());
        self.population = nextPopuluation;
    
        