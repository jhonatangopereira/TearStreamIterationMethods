# -*- coding: utf-8 -*-
"""
@author: Ana Vitória Santos Marques
"""

import pandas as pd


x = 0.65
data = []
for i in range(1, 2000+1):
  if i == 1:
    #alimentação
    nc8h10a = 100 
    nc8h8a = 0
    nh2a = 0 
    nh2oa = 3000 
    ntotala = nc8h10a + nc8h8a + nh2a + nh2oa
    
    #reciclo
    nc8h10r = 0 
    nc8h8r = 0
    nh2r = 0 
    nh2or = 0 
    ntotalr = nc8h10r + nc8h8r + nh2r + nh2or

    #reator - entrada
    nc8h10ri = nc8h10a + nc8h10r
    nc8h8ri = nc8h8a + nc8h8r
    nh2ri = nh2a + nh2r
    nh2ori = nh2oa + nh2or
    ntotalri = nc8h10ri + nc8h8ri + nh2ri + nh2ori

    #reator - saída
    nc8h10ro = nc8h10ri - (x * nc8h10ri)
    nc8h8ro = nc8h8ri + (x * nc8h10ri)
    nh2ro = nh2ri + (x * nc8h10ri)
    nh2oro = nh2ori
    ntotalro = nc8h10ro + nc8h8ro + nh2ro + nh2oro

    #água saída
    nc8h10w = nc8h10ro * 0
    nc8h8w = nc8h8ro * 0
    nh2w = nh2ro * 0
    nh2ow = nh2oro * 1
    ntotalw = nc8h10w + nc8h8w + nh2w + nh2ow

    #vapor - saída
    nc8h10v = nc8h10ro * 0
    nc8h8v = nc8h8ro * 0
    nh2v = nh2ro * 1
    nh2ov = nh2oro * 0
    ntotalv = nc8h10v + nc8h8v + nh2v + nh2ov

    #organic out
    nc8h10oo = nc8h10ro * 1
    nc8h8oo = nc8h8ro * 1
    nh2oo = nh2ro * 0
    nh2ooo = nh2oro * 0
    ntotaloo = nc8h10oo + nc8h8oo + nh2oo + nh2ooo

    #product
    nc8h10p = nc8h10oo * 0.01
    nc8h8p = nc8h8oo * 0.99
    nh2p = nh2ro * 0
    nh2op = nh2oro * 0
    ntotalp = nc8h10p + nc8h8p + nh2p + nh2op

    #reciclo
    ebzr = nc8h10oo - nc8h10p
    strr = nc8h8oo - nc8h8p
    h2r = nh2oo - nh2p
    watr = nh2ooo - nh2op
    ntotalre = ebzr + strr + h2r + watr
    
  else: 
    # for c in range(1, 2000+1):
    #   #reciclo
    nc8h10r = ebzr 
    nc8h8r = strr
    nh2r = h2r 
    nh2or = watr
            
    # Reator - entrada    
    nc8h10ri = nc8h10a + nc8h10r
    nc8h8ri = nc8h8a + nc8h8r
    nh2ri = nh2a + nh2r
    nh2ori = nh2oa + nh2or
    ntotalr = nc8h10r + nc8h8r + nh2r + nh2or
    ntotalri = nc8h10ri + nc8h8ri + nh2ri + nh2ori
    
    # Reator - saidda 
    nc8h10ro = nc8h10ri - (x * nc8h10ri)
    nc8h8ro = nc8h8ri + (x * nc8h10ri)
    nh2ro = nh2ri + (x * nc8h10ri)
    nh2oro = nh2ori
    ntotalro = nc8h10ro + nc8h8ro + nh2ro + nh2oro
    
    #água saída
    nc8h10w = nc8h10ro * 0
    nc8h8w = nc8h8ro * 0
    nh2w = nh2ro * 0
    nh2ow = nh2oro * 1
    ntotalw = nc8h10w + nc8h8w + nh2w + nh2ow

    #vapor - saída
    nc8h10v = nc8h10ro * 0
    nc8h8v = nc8h8ro * 0
    nh2v = nh2ro * 1
    nh2ov = nh2oro * 0
    ntotalv = nc8h10v + nc8h8v + nh2v + nh2ov

    #organic out
    nc8h10oo = nc8h10ro * 1
    nc8h8oo = nc8h8ro * 1
    nh2oo = nh2ro * 0
    nh2ooo = nh2oro * 0
    ntotaloo = nc8h10oo + nc8h8oo + nh2oo + nh2ooo

    #product
    nc8h10p = nc8h10oo * 0.01
    nc8h8p = nc8h8oo * 0.99
    nh2p = nh2ro * 0
    nh2op = nh2oro * 0
    ntotalp = nc8h10p + nc8h8p + nh2p + nh2op

    #reciclo
    ebzr = nc8h10oo - nc8h10p
    strr = nc8h8oo - nc8h8p
    h2r = nh2oo - nh2p
    watr = nh2ooo - nh2op
    ntotalre = ebzr + strr + h2r + watr

data.append([nc8h10a, nc8h10r, nc8h10ri, nc8h10ro, nc8h10w, nc8h10v, nc8h10oo, nc8h10p, ebzr])
data.append([nc8h8a, nc8h8r, nc8h8ri, nc8h8ro, nc8h8w, nc8h8v, nc8h8oo, nc8h8p, strr])
data.append([nh2a, nh2r, nh2ri, nh2ro, nh2w, nh2v, nh2oo, nh2p, h2r])
data.append([nh2oa, nh2or, nh2ori, nh2oro, nh2ow, nh2ov, nh2ooo, nh2op, watr])
data.append([ntotala, ntotalr, ntotalri, ntotalro, ntotalw, ntotalv, ntotaloo, ntotalp, ntotalre])

df = pd.DataFrame(data=data, index=["N(C8H10)", "N(C8H8)", "N(H2)", "N(H2O)", "N(total)"], columns=["Feed", "Recycle", "Reactor_In", "Reactor_Out", "Water_Out", "Vapor_Out", "Organic_Out", "Product", "New Recycle"])
print("Vazão de cada componente em mol/h:")
print(df)
