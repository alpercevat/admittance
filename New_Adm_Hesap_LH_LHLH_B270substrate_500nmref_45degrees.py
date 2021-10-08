#%%
#* Two layers (L)+(H) 45 degrees

import numpy as np
import math
from matplotlib import pyplot as plt

n0 = 1
nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi
V0 = math.radians(45)
V1 = np.arcsin((n0/nlayerL)*math.sin(V0))
V2 = np.arcsin((n0/nlayerH)*math.sin(V0))
V3 = np.arcsin((n0/nsub)*math.sin(V0))

for i in range(0,202):

    if  i < 101:
        sigmalayer = (twopi*i*1e-9*nlayerL*math.cos(V1))/lamda

        m1 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V1))*math.sin(sigmalayer))],
                       [(1j*nlayerL*math.cos(V1))*math.sin(sigmalayer),math.cos(sigmalayer)]])


        b = m1[0][0] + m1[0][1]*(nsub*math.cos(V3))
        c = m1[1][0] + m1[1][1]*(nsub*math.cos(V3))
        y = c/b

        #print(y.real)
    elif i == 101:
        i = i - 1
        sigmalayer = (twopi*i*1e-9*nlayerL*math.cos(V1))/lamda

        m1 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V1))*math.sin(sigmalayer))],
                       [(1j*nlayerL*math.cos(V1))*math.sin(sigmalayer),math.cos(sigmalayer)]])


        b = m1[0][0] + m1[0][1]*(nsub*math.cos(V3))
        c = m1[1][0] + m1[1][1]*(nsub*math.cos(V3))
        y = c/b

    elif i > 101:
        i = i - 101
        sigmalayer = (twopi*i*1e-9*nlayerH*math.cos(V2))/lamda

        m2 = np.array([[math.cos(sigmalayer),(1j/(nlayerH*math.cos(V2)))*math.sin(sigmalayer)],
                   [(1j*nlayerH*math.cos(V2))*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m3 = np.matmul(m2,m1)


        b = m3[0][0] + m3[0][1]*(nsub*math.cos(V3))
        c = m3[1][0] + m3[1][1]*(nsub*math.cos(V3))
        y = c/b

    plt.plot(y.real,y.imag , 'r.-')
    plt.xlabel("Real Part")
    plt.ylabel("İmaginer Part") 
    plt.title(" LH - B270 substrate - 45 Degrees ")

    print(y.real)
    

# %%
#* Four layers (L)+(H)+(L)+(H) 45 degrees

import numpy as np
import math
from matplotlib import pyplot as plt

n0 = 1
nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi
V0 = math.radians(45)
V1 = np.arcsin((n0/nlayerL)*math.sin(V0))
V2 = np.arcsin((n0/nlayerH)*math.sin(V0))
V3 = np.arcsin((n0/nsub)*math.sin(V0))
V4 = np.arcsin((n0/nlayerL)*math.sin(V0))
V5 = np.arcsin((n0/nlayerH)*math.sin(V0))

for i in range(0,404):

    if  i < 101:
        sigmalayer = (twopi*i*1e-9*nlayerL*math.cos(V1))/lamda

        m1 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V1))*math.sin(sigmalayer))],
                       [(1j*nlayerL*math.cos(V1))*math.sin(sigmalayer),math.cos(sigmalayer)]])


        b = m1[0][0] + m1[0][1]*(nsub*math.cos(V3))
        c = m1[1][0] + m1[1][1]*(nsub*math.cos(V3))
        y = c/b

        #print(y.real)

    elif i == 101:   # Ara Katman
        i = i - 1
        sigmalayer = (twopi*i*1e-9*nlayerL*math.cos(V1))/lamda

        m1 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V1))*math.sin(sigmalayer))],
                       [(1j*nlayerL*math.cos(V1))*math.sin(sigmalayer),math.cos(sigmalayer)]])


        b = m1[0][0] + m1[0][1]*(nsub*math.cos(V3))
        c = m1[1][0] + m1[1][1]*(nsub*math.cos(V3))
        y = c/b


    elif i > 101 and i<202:
        i = i - 101
        sigmalayer = (twopi*i*1e-9*nlayerH*math.cos(V2))/lamda

        m2 = np.array([[math.cos(sigmalayer),(1j/(nlayerH*math.cos(V2)))*math.sin(sigmalayer)],
                       [(1j*nlayerH*math.cos(V2))*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m3 = np.matmul(m2,m1)


        b = m3[0][0] + m3[0][1]*(nsub*math.cos(V3))
        c = m3[1][0] + m3[1][1]*(nsub*math.cos(V3))
        y = c/b

    elif i == 202:
        i = i - 102
        sigmalayer = (twopi*i*1e-9*nlayerH*math.cos(V2))/lamda

        m2 = np.array([[math.cos(sigmalayer),(1j/(nlayerH*math.cos(V2)))*math.sin(sigmalayer)],
                       [(1j*nlayerH*math.cos(V2))*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m3 = np.matmul(m2,m1)


        b = m3[0][0] + m3[0][1]*(nsub*math.cos(V3))
        c = m3[1][0] + m3[1][1]*(nsub*math.cos(V3))
        y = c/b

    elif i > 202 and i<303 :
        i = i - 202
        sigmalayer = (twopi*i*1e-9*nlayerL*math.cos(V4))/lamda

        m4 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V4)))*math.sin(sigmalayer)],
                       [(1j*nlayerL*math.cos(V4))*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m5 = np.matmul(m4,m3)

        b = m5[0][0] + m5[0][1]*(nsub*math.cos(V3))
        c = m5[1][0] + m5[1][1]*(nsub*math.cos(V3))
        y = c/b

    elif i == 303:
        i = i - 203
        sigmalayer = (twopi*i*1e-9*nlayerL*math.cos(V4))/lamda

        m4 = np.array([[math.cos(sigmalayer),(1j/(nlayerL*math.cos(V4)))*math.sin(sigmalayer)],
                       [(1j*nlayerL*math.cos(V4))*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m5 = np.matmul(m4,m3)

        b = m5[0][0] + m5[0][1]*(nsub*math.cos(V3))
        c = m5[1][0] + m5[1][1]*(nsub*math.cos(V3))
        y = c/b


    elif i > 303:
        i = i - 303
        sigmalayer = (twopi*i*1e-9*nlayerH*math.cos(V5))/lamda

        m6 = np.array([[math.cos(sigmalayer),(1j/(nlayerH*math.cos(V5)))*math.sin(sigmalayer)],
                   [(1j*nlayerH*math.cos(V5))*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m7 = np.matmul(m6,m5)


        b = m7[0][0] + m7[0][1]*(nsub*math.cos(V3))
        c = m7[1][0] + m7[1][1]*(nsub*math.cos(V3))
        y = c/b

    plt.plot(y.real,y.imag , 'r.-')
    plt.xlabel("Real Part")
    plt.ylabel("İmaginer Part") 
    plt.title(" LHLH - B270 substrate - 45 degrees ")

    print(y.real)
    

# %%
