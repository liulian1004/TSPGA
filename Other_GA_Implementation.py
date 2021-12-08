#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:51:58 2021

@author: liulian
"""
import random

from LIFE import Life

class Other_GA_Implementation(object):
    
    population = [];
    counts = 0;
    sample = 0;
    best = None;
    evulationFuntion = None;
    distanceMatrix = None;
    crossoverRate = 0.6;
    mutationRate = 0.001;
    bounds = 0;
    
    def __init__(self, counts, samples, distanceMatrix):
        self.counts = counts;
        self.samples = samples;
        self.distanceMatrix = distanceMatrix;
        self.initPopulation();


    def initPopulation(self):
        self.population = [];
        
        for i in range(self.samples):
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
        
        
        
    def crossOver(self, parent1, parent2):
        index1 = random.randint(1, self.counts-2);
        index2 = random.randint(index1, self.counts-2)
        tempGene = parent2.route[index1:index2];
        child = [];
        child.append(0);
        p1 = 1;
        for city in parent1.route:
            if city == 0:
                continue;
            if p1 == index1:
                child.extend(tempGene)
            if city not in tempGene:
                child.append(city)
            p1 += 1;
        child.append(0);
        return Life(child);


    def mutation(self, child):
         index1 = random.randint(1, len(child.route)-2);
         index2 = random.randint(1, len(child.route)-2);
         child.route[index1], child.route[index2] = child.route[index2],child.route[index1];
         return child;
    

    def calculateRate(self, life):
        distance = 0.0
        for i in range(0, len(life.route)-1):
            index1, index2 = life.route[i], life.route[i+1]
            distance += self.distanceMatrix[index1,index2];
            
        life.distance = distance;
        return 1/distance;
    
    
    def evaluation(self):
        self.bounds = 0;
        self.best = self.population[0];
        for life in self.population:
            life.rate = self.calculateRate(life);
            self.bounds += life.rate
            if self.best.rate < life.rate:
                self.best = life;


    def pickUpParent(self):
        r = random.uniform(0, self.bounds)
        for life in self.population:
            r -= life.rate;
            if r <= 0:
                return life;
        
    

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
    

    def nextGeneration(self):
        self.evaluation();
        self.population = sorted(self.population, key = lambda x: x.distance)
        nextPopuluation = [];
        fromOrig = self.population[:1];
        nextPopuluation.extend(fromOrig);
        while len(nextPopuluation) < self.samples:
            nextPopuluation.append(self.generateChild());
        self.population = nextPopuluation;
   