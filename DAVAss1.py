# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:30:23 2018

@author: Abhishek
"""
import numpy as np


def feature_sign(A,y,g):
    y=np.array(y)
    dim=np.shape(A)
    x=np.zeros([dim(1),1])
    theta=np.sign(x)
    act_set=[]
    for i in range(100):
        D=0
        index=0
        for j in range(dim(1)):
            ai=np.tranpose(A)[j]
            ai=np.reshape(ai,[np.shape(ai)[0],1])
            d=np.matmul(ai,y)
            d=d-(np.matmul(ai,np.matmul(A,y)))
            d=abs(d)
            if D<d:
                index=j
                D=d
        act_set.append(index)
        if D>g:
            theta[index]=-1
        else:
            theta[index]=1
        act_set.append(i)
    return x
