# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:17:24 2021

@author: Kurniawan
"""
import pandas as panda

class classData:
    __data = None
    
    def __init__(self):
        self.__readExcel()
    
    def getData(self):
        return self.__data
    #
    # def getDataI(self,i):
    #     print(self.__data[i])
    #
    def getDist(self,i,j):
        # i index data ke-1
        # j index data ke-2
        data = self.__data
        data1 = data[i]
        data2 = data[j]
        nFitur = len(data1)
        dist = 0
        for k in range (nFitur):
            dist = dist+(abs(data1[k]-data2[k]))
        return dist
    
    def __readExcel(self):
        file = panda.read_excel(open('data.xlsx','rb'))
        df = panda.DataFrame(file,columns=(['x','y']))
        dataset = df.values.tolist()
        self.__data = dataset