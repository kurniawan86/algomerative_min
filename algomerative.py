# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 13:19:29 2021

@author: Kurniawan
"""

from cluster import classCluster
class algomerative:
    cs=classCluster()
    tipe=None
    nCluster=9
    
    def __init__(self,nCluster,tipe):
        self.nCluster=nCluster
        self.tipe=tipe
        self.iterative()
    
    def iterative(self):
        cluster=self.cs.getClusterIndex()
        n=len(cluster)
        print(n)
        print(cluster)
        
        #loop all cluster
        for k in range (n-self.nCluster):
            if self.tipe=='min':
                i,j=self.cs.findMinIndxCluster()
            elif self.tipe=='max':
                i,j=self.cs.findMaxIndxCluster()
            self.cs.joinCluster(i, j)
            print(cluster)

nCluster=3
algo=algomerative(nCluster,'min')