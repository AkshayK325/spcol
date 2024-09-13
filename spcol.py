# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:44:15 2021

@author: akumar242
"""
import numpy as np


def N(x, d, i, t):   
    if d == 0:              
       if t[i] <= x < t[i+1] :
           c1 = 1.0;
           c2 = 0.0;
       elif x == t[-1] and t[i] < x <= t[i+1] :
           c1 = 0.0;
           c2 = 1.0;
       else: 
           c1 = 0.0;
           c2 = 0.0;          
    else:         
       if t[i+d] == t[i]:
          c1 = 0.0
       else:
          c1 = (x - t[i])/(t[i+d] - t[i]) * N(x, d-1, i, t)
       if t[i+d+1] == t[i+1]:
          c2 = 0.0
       else:
          c2 = (t[i+d+1] - x)/(t[i+d+1] - t[i+1]) * N(x, d-1, i+1, t)

    return c1 + c2

def dN(x, d, i, t):
   if d == 0:
      return 0.0 if t[i] <= x < t[i+1] else 0.0
   if t[i+d] == t[i]:
      c1 = 0.0
   else:
      c1 = (d)/(t[i+d] - t[i]) * N(x, d-1, i, t)
   if t[i+d+1] == t[i+1]:
      c2 = 0.0
   else:
      c2 = (d)/(t[i+d+1] - t[i+1]) * N(x, d-1, i+1, t)

   return c1 - c2


def ddN(x, d, i, t, k):
   if k == 1:
      c=dN(x, d, i, t)
      return c
   if t[i+d] == t[i]:
      c1 = 0.0
   else:
      c1 = (d)/(t[i+d] - t[i]) * ddN(x, d-1, i, t,k-1)
   if t[i+d+1] == t[i+1]:
      c2 = 0.0
   else:
      c2 = (d)/(t[i+d+1] - t[i+1]) * ddN(x, d-1, i+1, t,k-1)

   return c1 - c2


def findspan(t,x):
    l = np.searchsorted(t, x);
    if t[l] == t[0]:
        l = np.searchsorted(t, x,side='right');    
    return l

def spcol(U,d,u):
    Unq_U = np.array(np.unique(U))
    coll = np.zeros([len(u), len(Unq_U)-1+d])
    
    Sort_u = np.sort(u)
    
    Unq_u, count_u = np.unique(Sort_u, return_counts=True)
    
    k = -1
    for i in range(0, len(Unq_u)):
        k = k+1
        l = findspan(U,Unq_u[i]);
        for ii in range(l-d-1,l):   
            coll[k, ii] = N(Unq_u[i], d, ii, U)
            
        
        if count_u[i] > 1:
            for j in range(1, count_u[i]):
                k = k+1
                for ii in range(l-d-1,l):
                    coll[k, ii] = ddN(Unq_u[i], d, ii, U,j);
    return coll


# Test variables
# U=np.array([0,0,0,0,0.25,0.5,0.75,1,1,1,1]);
# p=3;

# u=np.array([0,0.25,0.5,0.75,1,1]);
# # u=np.array([0,1])
# # U=np.array([0,0,1,1]);
# # p=1;

# M=spcol(U,p,u);
# print(M);


