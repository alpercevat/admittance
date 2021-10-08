#%%
#* One single Layer (L)

import numpy as np
import math

n0 = 1
nlayer = 1.5
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi
V0 = math.radians(30)
V1 = np.arcsin((n0/nlayer)*math.sin(V0))
V2 = np.arcsin((n0/nsub)*math.sin(V0))

for i in range(0,101):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayer*math.cos(V1))/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/(nlayer*math.cos(V1))*math.sin(sigmalayer))],
                   [(1j*nlayer*math.cos(V1))*math.sin(sigmalayer),math.cos(sigmalayer)]])


    b = m1[0][0] + m1[0][1]*(nsub*math.cos(V2))
    c = m1[1][0] + m1[1][1]*(nsub*math.cos(V2))
    y = c/b
    
    print(y.imag)

#%%
#* Two layers with angle  (L)+(H)

import numpy as np
import math

n0 = 1
nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi
V0 = math.radians(30)
V1 = np.arcsin((n0/nlayerL)*math.sin(V0))
V2 = np.arcsin((n0/nlayerH)*math.sin(V0))
V3 = np.arcsin((n0/nsub)*math.sin(V0))

for i in range(0,101):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayerL*math.cos(V1))/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V1))*math.sin(sigmalayer))],
                   [(1j*nlayerL*math.cos(V1))*math.sin(sigmalayer),math.cos(sigmalayer)]])


    b = m1[0][0] + m1[0][1]*(nsub*math.cos(V3))
    c = m1[1][0] + m1[1][1]*(nsub*math.cos(V3))
    y = c/b
    
    print(y.real)


for k in range(0,101):
    laythic = k
    sigmalayer = (twopi*laythic*1e-9*nlayerH*math.cos(V2))/lamda

    m2 = np.array([[math.cos(sigmalayer),(1j/(nlayerH*math.cos(V2)))*math.sin(sigmalayer)],
                   [(1j*nlayerH*math.cos(V2))*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m3 = np.matmul(m2,m1)


    b = m3[0][0] + m3[0][1]*(nsub*math.cos(V3))
    c = m3[1][0] + m3[1][1]*(nsub*math.cos(V3))
    y = c/b

    print(y.real)

# %%
#* Four layers with angle  (L)+(H)+(L)+(H)

import numpy as np
import math

n0 = 1
nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi
V0 = math.radians(30)
V1 = np.arcsin((n0/nlayerL)*math.sin(V0))
V2 = np.arcsin((n0/nlayerH)*math.sin(V0))
V3 = np.arcsin((n0/nsub)*math.sin(V0))
V4 = np.arcsin((n0/nlayerL)*math.sin(V0))
V5 = np.arcsin((n0/nlayerH)*math.sin(V0))

for i in range(0,101):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayerL*math.cos(V1))/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V1))*math.sin(sigmalayer))],
                   [(1j*nlayerL*math.cos(V1))*math.sin(sigmalayer),math.cos(sigmalayer)]])


    b = m1[0][0] + m1[0][1]*(nsub*math.cos(V3))
    c = m1[1][0] + m1[1][1]*(nsub*math.cos(V3))
    y = c/b
    
    print(y.imag)


for k in range(0,101):
    laythic = k
    sigmalayer = (twopi*laythic*1e-9*nlayerH*math.cos(V2))/lamda

    m2 = np.array([[math.cos(sigmalayer),(1j/(nlayerH*math.cos(V2)))*math.sin(sigmalayer)],
                   [(1j*nlayerH*math.cos(V2))*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m3 = np.matmul(m2,m1)


    b = m3[0][0] + m3[0][1]*(nsub*math.cos(V3))
    c = m3[1][0] + m3[1][1]*(nsub*math.cos(V3))
    y = c/b

    print(y.imag)

for l in range(0,101):
    laythic = l
    sigmalayer = (twopi*laythic*1e-9*nlayerL*math.cos(V4))/lamda

    m4 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V4)))*math.sin(sigmalayer)],
                   [(1j*nlayerL*math.cos(V4))*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m5 = np.matmul(m4,m3)

    b = m5[0][0] + m5[0][1]*(nsub*math.cos(V3))
    c = m5[1][0] + m5[1][1]*(nsub*math.cos(V3))
    y = c/b

    print(y.imag)

for t in range(0,101):
    laythic = t
    sigmalayer = (twopi*laythic*1e-9*nlayerH*math.cos(V5))/lamda

    m6 = np.array([[math.cos(sigmalayer),(1j/(nlayerH*math.cos(V5)))*math.sin(sigmalayer)],
                   [(1j*nlayerH*math.cos(V5))*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m7 = np.matmul(m6,m5)


    b = m7[0][0] + m7[0][1]*(nsub*math.cos(V3))
    c = m7[1][0] + m7[1][1]*(nsub*math.cos(V3))
    y = c/b

    print(y.imag)


# %%
