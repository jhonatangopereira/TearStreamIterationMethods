# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:20:06 2022

@author: anavi
"""
from scipy.optimize import fsolve


def wegstein_model(x) -> float:
    nc8h10a = 100
    nc8h8a = 0
    nh2a = 0 
    nh2oa = 3000         
    nc8h10r = x 
    nc8h8r = 1.00469113
    nh2r = 0
    nh2or = 0
    nc8h10ri = nc8h10a + nc8h10r
    nc8h8ri = nc8h8a + nc8h8r
    nh2ri = nh2a + nh2r
    nh2ori = nh2oa + nh2or
    nc8h10ro = nc8h10ri - (0.65 * nc8h10ri)
    nc8h8ro = nc8h8ri + (0.65 * nc8h10ri)
    nh2ro = nh2ri + (0.65 * nc8h10ri)
    nh2oro = nh2ori
    nh2ow = nh2oro * 1
    nh2v = nh2ro * 1
    nc8h10oo = nc8h10ro * 1
    nc8h8oo = nc8h8ro * 1
    nc8h10p = nc8h10oo * 0.01
    nc8h8p = nc8h8oo * 0.99
    f = nc8h10a * 106.167 + nh2oa*18.01 - nh2ow*18.01 - nh2v*2.016 - nc8h10p*106.167 - nc8h8p*104.15

    return f

sol = fsolve(wegstein_model, 50)
print(sol)
