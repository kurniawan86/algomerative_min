# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:23:13 2021

@author: Kurniawan
"""
from data import classData

class classCluster:
    cData = classData()
    __clusterData = []
    __clusterIndex = []
    
    def __init__(self):
        #initiliasasi data and cluster
        data=self.cData.getData()
        self.__initClusterIndex(data)
    
    def getClusterData(self):
        return self.__clusterData
    
    def getClusterIndex(self):
        return self.__clusterIndex
    
    def __initClusterData(self,data):
        bar = len(data)
        clusters = []
        for i in range(bar):
            cluster=[]
            cluster.append(data[i])
            clusters.append(cluster)
        self.__clusterData=cluster
    
    def __initClusterIndex(self,data):
        bar = len(data)
        for i in range(bar):
            cluster = []
            cluster.append(i+1)
            self.__clusterIndex.append(cluster)
    
    def joinCluster(self,i,j):
        # i adalah index data tujuan join
        # j adalah index data yang dijoinkan
        cluster = self.__clusterIndex
        nlist = len(cluster[j])
        if nlist == 1:
            cluster[i].append(cluster[j][0])
        else:
            for k in range (nlist):
                cluster[i].append(cluster[j][k])
        cluster.pop(j)
    
    def joinClusterData(self,i,j):
        # i adalah index data tujuan join
        # j adalah index data yang dijoinkan
        cluster=self.__clusterData
        nlist=len(cluster[j])
        if nlist==1:
            cluster[i].append(cluster[j][0])
        else:
            for k in range (nlist):
                cluster[i].append(cluster[j][k])
        cluster.pop(j)
        
    def calMinDist(self,i,j):
        # i index ke-1 cluster
        # j index ke-2 cluster
        clust=self.__clusterIndex
        m=len(clust[i])
        n=len(clust[j])
        min0=self.cData.getDist(clust[i][0]-1,clust[j][0]-1)
        for t in range(m):
            for r in range (n):
                min1=self.cData.getDist(clust[i][t]-1,
                                        clust[j][r]-1)
                if min1<min0:
                    min0=min1
        return min0
    
    def findMinIndxCluster(self):
        cs=self.__clusterIndex
        n=len(cs)
        minVal1=self.calMinDist(0, 1)
        indx1=0
        indx2=1
        for i in range (1,n):
            for j in range(i+1,n):
                minVal2=self.calMinDist(i, j)
                if minVal1>minVal2:
                    minVal1=minVal2
                    indx1=i
                    indx2=j
        return indx1,indx2