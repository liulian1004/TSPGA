#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:14:44 2021

@author: liulian
"""
import random

class GA(object):
    population = [];
    
    def __init__(self, counts, sample):
        self.counts = counts;
        self.sample = sample;
        self.initPopulation();
        
    
    
    """  
    generate the sample number of random path, current I will generate 100 sample
    ex: one of random path:[0,1,2,3,0]
    """
    def initPopulation(self):
        self.population = [];
        
        for i in range(self.sample):
            # here shall exclude the start city, which I will append manually
            cities = list(range(self.counts-1));
            random.shuffle(cities);
            curPop = [];
            curPop.append(0);
            for number in cities:
                number += 1;
                curPop.append(number);
            curPop.append(0);
            self.population.append(curPop);
            
        
        #print(self.population)
        
        