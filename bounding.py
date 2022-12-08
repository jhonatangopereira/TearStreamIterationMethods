# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:01:32 2022

@author: anavi
"""
x0 = 200
dx = 50


def Fun(x0):
    return (x0 - 0.9)**2


def bounding(x0, dx):
    f0 = Fun(x0)
    xesq = x0 - dx
    fesq = Fun(xesq)
    xdir = x0 + dx
    fdir = Fun(xdir)

    iterx = 0
    itermax = 7
    
    while iterx < itermax:
        if fesq > f0  and  fdir > f0: 
               break
           
        elif f0 > fdir:
            iterx = iterx + 1
            xesq = x0
            fesq=f0
            x0 = xdir
            f0 = fdir
            xdir = x0 + (2**iterx)*dx
            fdir = Fun(xdir)
            print(fdir)
            
        else:
            iterx = iterx + 1
            xdir = x0
            fdir = x0
            x0 = xesq
            f0 = fesq
            xesq = x0 - (2**iterx)*dx
            fesq = Fun(xesq)
            print(fesq)
    
    return [fdir, fesq]
    
        
print(bounding(x0, dx))
