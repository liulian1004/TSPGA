#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:58:56 2021

@author: liulian
"""

class Life():
    rate = 0;
    distance = 0;
    route = [];
    def __init__(self, route):
        self.rate = 0;
        self.distance = 0;
        self.route = route;