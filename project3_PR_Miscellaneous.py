# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:00:06 2018

@author: eric.c.c
"""
from utils import readfile, readdataset, readdatasetcsv, HubsAuthorities, PageRank, SimRank, addEdge, deleteEdge, getOrderByDesc
import numpy as np

ga = readdataset('hw3dataset')
g1 = ga[0]
g2 = ga[1]
g3 = ga[2]
dumpingFactor = 0.15
########################################################################
#                               Graph_1                                #
########################################################################
print('############################################################')
print('Graph_1')
print(g1)
print('PageRank:')
pr = PageRank(g1, dumpingFactor = dumpingFactor)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
print('Graph_11 (add edge(6,1)) ==> increase auth of node1')
g11 = np.array(g1)
addEdge(g11, 6, 1)
print(g11)
pr = PageRank(g11, dumpingFactor = dumpingFactor)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('############################################################')
########################################################################
#                               Graph_2                                #
########################################################################
print('############################################################')
print('Graph_2')
print(g2)
print('PageRank:')
pr = PageRank(g2, dumpingFactor = dumpingFactor)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
print('Graph_21 (add edge(6,1)) ==> increase auth of node1')
g21 = np.array(g2)
addEdge(g21, 4, 1)
print(g21)
pr = PageRank(g21, dumpingFactor = dumpingFactor)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('############################################################')
########################################################################
#                               Graph_3                                #
########################################################################
print('############################################################')
print('Graph_3')
print(g3)
print('PageRank:')
pr = PageRank(g3, dumpingFactor = dumpingFactor)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
print('Graph_31 (add edge(3,1)) ==> increase auth of node1')
g31 = np.array(g3)
addEdge(g31, 3, 1)
print(g31)
pr = PageRank(g31, dumpingFactor = dumpingFactor)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('############################################################')
''''''