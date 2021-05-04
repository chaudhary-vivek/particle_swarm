#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 14:54:37 2021

@author: vivek
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:18:32 2021

@author: vivek
"""
import random
import math
import numpy as np

class Node(object):
    def __init__(self, node_type, number, fix_cost, capacity):
        self.node_type = node_type
        self.number = number
        self.fix_cost = fix_cost
        self.capacaity = capacity        
    def getname(self):
        name = str(self.node_type)+ str(self.number)
        return name
        return self.name
    def getnumber(self):
        return self.number
    def getfix_cost(self):
        return self.fix_cost
    def getcapacity(self):
        return self.capacity
nodes = {}
nodes['1'] = Node('sup', 1, 900, 250)
nodes['2'] = Node('sup', 2, 500, 200)
nodes['3'] = Node('sup', 3, 1300, 250)
nodes['4'] = Node('plant', 1, 1300, 150)
nodes['5'] = Node('plant', 2, 1000, 250)
nodes['6'] = Node('plant', 3, 750, 200)
nodes['7'] = Node('plant', 4, 0, 0)
nodes['8'] = Node('dc', 1, 1300, 150)
nodes['9'] = Node('dc', 2, 1000, 100)
nodes['10'] = Node('dc', 3, 950, 200)
nodes['11'] = Node('dc', 4, 1100, 150)
nodes['12'] = Node('dc', 5, 0, 0) 
nodes['13'] = Node('c', 1, 1300, 50)
nodes['14'] = Node('c', 2, 900, 100)
nodes['15'] = Node('c', 3, 990, 100)
nodes['16'] = Node('c', 4, 1000, 100)
nodes['17'] = Node('c', 5, 0, 0)


supplier_plant = {
        '(1,1)': 4,
        '(1,2)': 3,
        '(1,3)': 1,
        '(1,4)': 0,
        '(2,1)': 3,
        '(2,2)': 5,
        '(2,3)': 2,
        '(2,4)': 0,
        '(3,1)': 1,
        '(3,2)': 6,
        '(3,3)': 4,
        '(3,4)': 2,

        }

plant_dc = {
        '(1,1)': 5,
        '(1,2)': 2,
        '(1,3)': 4,
        '(1,4)': 3,
        '(1,5)': 0,
        '(2,1)': 4,
        '(2,2)': 6,
        '(2,3)': 3,
        '(2,4)': 5,
        '(2,5)': 0,
        '(3,1)': 3,
        '(3,2)': 5,
        '(3,3)': 1,
        '(3,4)': 6,
        '(3,5)': 0,
        }

dc_customer = {
        '(1,1)': 3,
        '(1,2)': 5,
        '(1,3)': 2,
        '(1,4)': 4,
        '(1,5)': 0,
        '(2,1)': 6,
        '(2,2)': 2,
        '(2,3)': 5,
        '(2,4)': 1,
        '(2,5)': 0,
        '(3,1)': 4,
        '(3,2)': 3,
        '(3,3)': 6,
        '(3,4)': 5,
        '(3,5)': 0,
        '(4,1)': 2,
        '(4,2)': 4,
        '(4,3)': 3,
        '(4,4)': 2,
        '(4,5)': 0,
        }



class Particle:
    def __init__(self):
        self.particle_position = []  # particle position
        self.particle_velocity = []  # particle velocity
        self.local_best_particle_position = []  # best position of the particle
        #self.fitness_local_best_particle_position = initial_fitness  # initial objective function value of the best particle position
        #self.fitness_particle_position = initial_fitness  # objective function value of the particle position 
        self.loc1 = nodes['1']
        self.loc2 = nodes['2']
        self.loc3 = nodes['3']
        self.loc4 = nodes['4']
        self.loc5 = nodes['5']
        self.loc6 = nodes['6']
        self.loc7 = nodes['7']
        self.loc8 = nodes['4']
        self.loc9 = nodes['5']
        self.loc10 = nodes['6']
        self.loc11 = nodes['8']
        self.loc12 = nodes['9']
        self.loc13 = nodes['10']
        self.loc14 = nodes['11']
        self.loc15 = nodes['12']
        self.loc16 = nodes['13']
        self.loc17 = nodes['14']
        self.loc18 = nodes['15']
        self.loc19 = nodes['16']
        self.loc20 = nodes['17']
        list1 = [1,2,3,4,5,6,7]
        list2 = [1,2,3,4,5,6,7,8]
        self.particle_position.extend(random.sample(list1, len(list1)))
        self.particle_position.extend(random.sample(list2, len(list2)))
        self.particle_position.extend(random.sample(range(1, 6), 5))        
    def getposition(self):
        return self.particle_position
    
y = Particle()
X = y.getposition()

'''
def objective_function(X):
    A = 10
    y = 0
    return y
'''

