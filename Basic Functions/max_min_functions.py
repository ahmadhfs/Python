# -*- coding: utf-8 -*-

# This Script contains minimum and maximum functions built from scratch

# Maximum Function :
def maximum(c):
    maxi = c[0]
    c_len = len(c)
    for i in range(0, c_len):
        if c[i] > maxi:
            maxi = c[i]
    return maxi

# Minimum Function :
def minimum(c):
    mini = c[0]
    c_len = len(c)
    for i in range(0, c_len):
        if c[i] < mini:
            mini = c[i]
    return mini

