#%%
#* One single Layer (L)

import numpy as np
import math

nlayer = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi

for i in range(0,201):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayer)/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/nlayer)*math.sin(sigmalayer)],
                   [(1j*nlayer)*math.sin(sigmalayer),math.cos(sigmalayer)]])


    b = m1[0][0] + m1[0][1]*nsub
    c = m1[1][0] + m1[1][1]*nsub 
    y = c/b
    
    print(y.real)

# %%
#* Two layers (L)+(H)

import numpy as np
import math

nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi

for i in range(0,101):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayerL)/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                   [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])


    b = m1[0][0] + m1[0][1]*nsub
    c = m1[1][0] + m1[1][1]*nsub 
    y = c/b
    
    z1 = y.real
    z2 = y.imag
    print(y.real)

for k in range(0,101):
    laythic = k
    sigmalayer = (twopi*laythic*1e-9*nlayerH)/lamda

    m2 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                   [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m3 = np.matmul(m2,m1)


    b = m3[0][0] + m3[0][1]*nsub
    c = m3[1][0] + m3[1][1]*nsub 
    y = c/b
    
    z3 = y.real
    z4 = y.imag
    print(y.real)



# %%

#* Four layers (L)+(H)+(L)+(H)


import numpy as np
import math

nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi

for i in range(0,101):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayerL)/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                   [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])


    b = m1[0][0] + m1[0][1]*nsub
    c = m1[1][0] + m1[1][1]*nsub 
    y = c/b
    
    print(y.imag)

for k in range(0,101):
    laythic = k
    sigmalayer = (twopi*laythic*1e-9*nlayerH)/lamda

    m2 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                   [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m3 = np.matmul(m2,m1)


    b = m3[0][0] + m3[0][1]*nsub
    c = m3[1][0] + m3[1][1]*nsub 
    y = c/b

    print(y.imag)


for l in range(0,101):
    laythic = l
    sigmalayer = (twopi*laythic*1e-9*nlayerL)/lamda

    m4 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                   [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m5 = np.matmul(m4,m3)

    b = m5[0][0] + m5[0][1]*nsub
    c = m5[1][0] + m5[1][1]*nsub 
    y = c/b

    print(y.imag)

for t in range(0,101):
    laythic = t
    sigmalayer = (twopi*laythic*1e-9*nlayerH)/lamda

    m6 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                   [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m7 = np.matmul(m6,m5)


    b = m7[0][0] + m7[0][1]*nsub
    c = m7[1][0] + m7[1][1]*nsub 
    y = c/b

    print(y.imag)





# %%
