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
########################################################################
#                               Graph_1                                #
########################################################################
print('############################################################')
print('Graph_1')
print(g1)
print('HITS:')
auth, hub = HubsAuthorities(g1)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
print('Graph_11 (add edge(6,1)) ==> increase auth of node1')
g11 = np.array(g1)
addEdge(g11, 6, 1)
print(g11)
auth, hub = HubsAuthorities(g11)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('######################')
print('Graph_12 (add edge(1,3)) ==> increase hub of node1')
g12 = np.array(g1)
addEdge(g12, 1, 3)
print(g12)
auth, hub = HubsAuthorities(g12)
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('############################################################')
########################################################################
#                               Graph_2                                #
########################################################################
print('############################################################')
print('Graph_2')
print(g2)
print('HITS:')
auth, hub = HubsAuthorities(g2)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
print('Graph_21 (add edge(4,1)) ==> increase auth of node1')
g21 = np.array(g2)
addEdge(g21, 4, 1)
print(g21)
auth, hub = HubsAuthorities(g21)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('######################')
print('Graph_22 (add edge(1,3)) ==> increase hub of node1')
g22 = np.array(g2)
addEdge(g22, 1, 3)
print(g22)
auth, hub = HubsAuthorities(g22)
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('############################################################')
########################################################################
#                               Graph_3                                #
########################################################################
print('############################################################')
print('Graph_3')
print(g3)
print('######################')
print('HITS:')
auth, hub = HubsAuthorities(g3)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('######################')
print('Graph_31 (add edge(4,1)) ==> increase auth of node1')
g31 = np.array(g3)
addEdge(g31, 4, 1)
print(g31)
auth, hub = HubsAuthorities(g31)
print('authority: ', auth)
print('order (by authority): ', getOrderByDesc(auth))
print('######################')
print('Graph_32 (add edge(1,3)) ==> increase hub of node1')
g32 = np.array(g3)
addEdge(g32, 1, 3)
print(g32)
auth, hub = HubsAuthorities(g32)
print('hub: ', hub)
print('order (by hub): ', getOrderByDesc(hub))
print('############################################################')
''''''