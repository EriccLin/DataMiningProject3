# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:05:58 2018

@author: linjiayuan
"""
import pandas as pd
import numpy as np
from numpy import linalg as la

def readfile(filepath, num_vertices):
    data = np.zeros(num_vertices * num_vertices)
    with open(filepath, 'r') as f:
        for line in f:
            v1, v2 = line.split(',')
            v1 = int(v1)
            v2 = int(v2)
            data[(v1-1)*num_vertices + v2-1] = 1
    return data.reshape((num_vertices, num_vertices))

def readdataset(filepath):
    graph_info = []
    with open((filepath + '/Read_me.txt'), 'r') as f:
        for line in f:
            if line.find('txt:') == -1 :
                continue
            start   = line.find('txt:') + 4
            mid     = line.find('nodes')
            end     = line.find('edges')
            v1 = int(line[start:mid])
            v2 = int(line[mid+6:end])
            graph_info.append([v1, v2])

    graph_all = []
    #read 6 graph data
    for i in range(1,7):
        graph = readfile(filepath + '/graph_%d.txt' %(i), graph_info[i-1][0])
        graph_all.append(graph)
    return graph_all

def readdatasetcsv(filepath = 'D:/pythonwork/datamining/data.csv', size = 20, bidirected = True):
    df = pd.read_csv(filepath)
    df.columns = ['transID', 'transID2', 'itemID']
    if size != None:
        df = df[:size]
    num_vertices = df.itemID.unique().shape[0]
    adjacencyMatrix = np.zeros((num_vertices,num_vertices), dtype = np.float32)
    itemID2UID = {itemid : idx for idx, itemid in enumerate(df.itemID.unique()) }
    for transid in df.transID.unique():
        itemset = np.asarray(df[df['transID'] == transid]['itemID'])
        itemsetSz = len(itemset)
        for i in range(itemsetSz-1):
            iUid = itemID2UID[itemset[i]]
            for j in np.arange(i, itemsetSz):
                jUid = itemID2UID[itemset[j]]
                adjacencyMatrix[iUid,jUid] = 1
                if bidirected == True:
                    adjacencyMatrix[jUid,iUid] = 1
    return adjacencyMatrix, itemID2UID
            

def HubsAuthorities(adjacencyMatrix, epsilon = 1e-5, maxIter = 30):
    adjacencyMatrix = np.array(adjacencyMatrix)
    num_vertices = adjacencyMatrix.shape[0]
    a_pre = np.ones(num_vertices).reshape((num_vertices,1))
    h_pre = np.ones(num_vertices).reshape((num_vertices,1))
    Iter = 0
    while True:
        a_cur = np.ones(num_vertices)
        h_cur = np.ones(num_vertices)
        a_cur = np.matmul(adjacencyMatrix.T, h_pre)
        h_cur = np.matmul(adjacencyMatrix  , a_pre)
        a_cur = a_cur/ la.norm(a_cur,2)
        h_cur = h_cur/ la.norm(h_cur,2)
        if (la.norm(a_pre - a_cur) + la.norm(h_pre - h_cur)) < epsilon or Iter > maxIter:
            break
        a_pre = a_cur
        h_pre = h_cur
        Iter = Iter + 1
    a_cur = a_cur.reshape(num_vertices)
    h_cur = h_cur.reshape(num_vertices)
    return a_cur, h_cur

def PageRank(adjacencyMatrix, dumpingFactor = 0.15, epsilon = 1e-5, maxIter = 30):
    AM = np.array(adjacencyMatrix)
    num_vertices = AM.shape[0]
    const = np.ones(num_vertices).reshape((num_vertices,1)) / num_vertices
    rank_pre = const    
    Iter = 0    
    for i in range(num_vertices):
        rowSum = sum(AM[i])
        if rowSum > 0:
            AM[i] = AM[i]/rowSum
        else:
            AM[i] = np.zeros((num_vertices,))
    AMT = AM.T
    while True:
        rank = dumpingFactor * const + (1 - dumpingFactor) * np.matmul(AMT, rank_pre)
        #print ( Iter, rank.reshape(num_vertices))
        if la.norm( rank_pre - rank ) < epsilon or Iter > maxIter:
            break
        rank_pre = rank
        Iter = Iter + 1
    rank = rank.reshape(num_vertices)
    return rank

def SimRank(adjacencyMatrix, C = 0.8, epsilon = 1e-5, maxIter = 30):
    AM = np.array(adjacencyMatrix, dtype = np.float32)
    num_vertices = AM.shape[0]
    Iter = 0
    AMT = AM.T
    for i in range(num_vertices):
        rowSum = sum(AMT[i])
        if rowSum > 0:
            AMT[i] = AMT[i]/sum(AMT[i])
        else:
            AMT[i] = np.zeros((num_vertices,))
    AM = AMT.T # column-wise normalized matrix
    #print(AM)
    S_pre = np.identity(num_vertices)    
    while True:    
        S = np.matmul( np.matmul(AMT, S_pre), AM) * C
        for i in range(num_vertices):
            S[i,i] = 1
        if la.norm(S_pre - S, 2) < epsilon or Iter > maxIter:
            break
        Iter = Iter + 1
    return S

def addEdge(adjacencyMatrix, fromeNode, toNode):
    v1 = fromeNode - 1
    v2 = toNode - 1
    adjacencyMatrix[v1,v2] = 1

def deleteEdge(adjacencyMatrix, fromeNode, toNode):
    v1 = fromeNode - 1
    v2 = toNode - 1
    adjacencyMatrix[v1,v2] = 0

def getOrderByDesc(arrays):
    return [ i[0]+1 for i in sorted(enumerate(arrays), key = lambda x: x[1], reverse = True)]





