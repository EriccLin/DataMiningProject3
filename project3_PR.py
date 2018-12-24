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
g4 = ga[3]
g5 = ga[4]
g6 = ga[5]
g7, g7dict = readdatasetcsv('D:/pythonwork/dataminingProject3/data.csv', size = 20, bidirected = True)
g8, g8dict = readdatasetcsv('D:/pythonwork/dataminingProject3/data.csv', size = 20, bidirected = False)
dump = 0.15
########################################################################
#                               Graph_1                                #
########################################################################
print('######################')
print('Graph_1')
print(g1)
print('PageRank:')
pr = PageRank(g1, dumpingFactor = dump)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
########################################################################
#                               Graph_2                                #
########################################################################
print('######################')
print('Graph_2')
print(g2)
print('PageRank:')
pr = PageRank(g2, dumpingFactor = dump)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
########################################################################
#                               Graph_3                                #
########################################################################
print('######################')
print('Graph_3')
print(g3)
print('PageRank:')
pr = PageRank(g3, dumpingFactor = dump)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
########################################################################
#                               Graph_4                                #
########################################################################
print('######################')
print('Graph_4')
print(g4)
print('PageRank:')
pr = PageRank(g4, dumpingFactor = dump)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
########################################################################
#                               Graph_5                                #
########################################################################
print('######################')
print('Graph_5')
print(g5)
print('PageRank:')
pr = PageRank(g5, dumpingFactor = dump)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
########################################################################
#                               Graph_6                                #
########################################################################
print('######################')
print('Graph_6')
print(g6)
print('PageRank:')
pr = PageRank(g6, dumpingFactor = dump)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
########################################################################
#                               Graph_7 (bidirected)                   #
########################################################################
print('######################')
print('Graph_7 (bidirected)')
print(g7)
print('PageRank:')
pr = PageRank(g7, dumpingFactor = dump)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')
########################################################################
#                               Graph_8 (directed)                     #
########################################################################
print('######################')
print('Graph_8 (directed)')
print(g8)
print('PageRank:')
pr = PageRank(g8, dumpingFactor = dump)
print('pr: ', pr)
print('order (by pr): ', getOrderByDesc(pr))
print('######################')

''''''