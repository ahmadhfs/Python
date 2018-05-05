# -*- coding: utf-8 -*-

# This Script contains sorting functions built from scratch

import max_min_functions

# Sorting Functions 1: 

def ordering(a, Type):
# a : Input array    
# Types : 
# A : Ascending, D :Descending
    
    out = []
    if Type == 'A':
        for i in range(0, len(a)):
            a_min = minimum(a) 
            out.insert(i,a_min)
            a.remove(a_min)
    if Type == 'D':
        for i in range(0, len(a)):
            a_max = maximum(a) 
            out.insert(i,a_max)
            a.remove(a_max)    
    return out

# Sorting Functions 2:

def selcting_sort(c, Type):
# a : Input array    
# Types : 
# A : Ascending, D :Descending 
    
    c_len = len(c)
    if Type == 'A':
        for i in range (0,c_len):
            min_indx = c.index(minimum(c[i:c_len]), i)
            tem = c[i]
            c[i] = c[min_indx]
            c[min_indx] = tem
    if Type == 'D':
        for i in range (0,c_len):
            max_indx = c.index(maximum(c[i:c_len]), i)
            tem = c[i]
            c[i] = c[max_indx]
            c[max_indx] = tem
    return c

