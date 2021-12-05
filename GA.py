#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:14:44 2021

@author: liulian
"""
import random

class GA(object):
    population = [];
    counts = 0;
    
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
        copyPart = parent2[index: len(parent2)-1];
        child = [];
        #child start with start city
        child.append(0);
        # P1 is the point pointer to the 1 index of parent1
        p1 = 1;
        for city in parent1:
            if city == 0:
                continue;
            if p1 == index:
                child.extend(copyPart)
            if city not in copyPart:
                child.append(city)
            p1 += 1;
        # child shall end at start city
        child.append(0);
        return child;
    
    
    def mutation(self, child):
         index1 = random.randint(1, len(child)-2);
         index2 = random.randint(1, len(child)-2);
         child[index1], child[index2] = child[index2],child[index1];
         return child;
                
def main():
    ga = GA(4,3);
    p1 = [0,1,2,3,0];
    p2 = [0,2,3,1,0];
    print(GA.crossOver(ga,p1, p2))
    print(GA.mutation(ga, p1))

if  __name__ == '__main__':
    main()

        