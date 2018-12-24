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
########################################################################
#                               Graph_1                                #
########################################################################
print('######################')
print('Graph_1')
print(g1)
print('HITS:')
auth, hub = HubsAuthorities(g1)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
########################################################################
#                               Graph_2                                #
########################################################################
print('######################')
print('Graph_2')
print(g2)
print('HITS:')
auth, hub = HubsAuthorities(g2)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
########################################################################
#                               Graph_3                                #
########################################################################
print('######################')
print('Graph_3')
print(g3)
print('HITS:')
auth, hub = HubsAuthorities(g3)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
########################################################################
#                               Graph_4                                #
########################################################################
print('######################')
print('Graph_4')
print(g4)
print('HITS:')
auth, hub = HubsAuthorities(g4)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
########################################################################
#                               Graph_5                                #
########################################################################
print('######################')
print('Graph_5')
print(g5)
print('HITS:')
auth, hub = HubsAuthorities(g5)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
########################################################################
#                               Graph_6                                #
########################################################################
print('######################')
print('Graph_6')
print(g6)
print('HITS:')
auth, hub = HubsAuthorities(g6)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
########################################################################
#                               Graph_7 (bidirected)                   #
########################################################################
print('######################')
print('Graph_7 (bidirected)')
print(g7)
print('HITS:')
auth, hub = HubsAuthorities(g7)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
########################################################################
#                               Graph_8 (directed)                     #
########################################################################
print('######################')
print('Graph_8 (directed)')
print(g8)
print('HITS:')
auth, hub = HubsAuthorities(g8)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')

''''''