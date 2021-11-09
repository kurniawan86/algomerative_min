# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 13:19:29 2021

@author: Kurniawan
"""

from cluster import classCluster
class algomerative:
    cs=classCluster()
    tipe = 'min'
    
    def __init__(self,nCluster):
        self.nCluster = nCluster
        self.iterative()
    
    def iterative(self):
        cluster = self.cs.getClusterIndex()
        n = len(cluster)
        print("proses iterasi ke - ", 0)
        print(cluster)
        print("")
        
        #loop all cluster
        for k in range (n-self.nCluster):
            if self.tipe == 'min':
                i,j = self.cs.findMinIndxCluster()
            self.cs.joinCluster(i, j)
            print("proses iterasi ke - ",k+1)
            print(cluster)
            print("")