# -*- coding: utf-8 -*-
"""
@author: anavi
"""
def Funcao(x0):
    return (x0 - 0.9)**2  

x0 = 200 
h = 1e-6
f0 = Funcao(x0)
dx = 50
xesq = x0 - dx
fesq = Funcao(xesq)
xdir = x0 + dx
fdir = Funcao(xdir)
i = 0 

while i < 10000:
    
    if fesq > f0 and  fdir > f0: 
           break
    if f0 > fdir: 
            i = i + 1
            xesq=x0
            fesq=f0
            x0 = xdir
            f0 = fdir
            xdir = x0 + (2**i)*dx
            fdir = Funcao(xdir)
            print(fdir)
    else: 
            i = i + 1
            xdir =x0
            fdir = x0
            x0 = xesq
            f0 = fesq
            xesq = x0 -(2**i)*dx
            fesq = Funcao(xesq)
            print(fesq)
            
for K in range(0, 6):
 
    EQ_Swann = x0 + (2 ** K) * dx
    print(EQ_Swann)
    for c in range(0, 6):
        x0 = EQ_Swann    