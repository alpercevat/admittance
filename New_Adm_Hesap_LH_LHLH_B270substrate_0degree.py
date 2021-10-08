#%%
#* Two layers (L)+(H)

import numpy as np
import math
from matplotlib import pyplot as plt

nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi

for i in range(0,201):

    if  i < 101:
        sigmalayer = (twopi*i*1e-9*nlayerL)/lamda

        m1 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                       [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])


        b = m1[0][0] + m1[0][1]*nsub
        c = m1[1][0] + m1[1][1]*nsub 
        y = c/b

        #print(y.real)

    elif i >= 101:
        i = i - 100
        sigmalayer = (twopi*i*1e-9*nlayerH)/lamda

        m2 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                       [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m3 = np.matmul(m2,m1)

        b = m3[0][0] + m3[0][1]*nsub
        c = m3[1][0] + m3[1][1]*nsub 
        y = c/b
        #print(m2)

    plt.plot(y.real,y.imag , 'r.-')
    plt.xlabel("Real Part")
    plt.ylabel("İmaginer Part") 
    plt.title(" LH - B270substrate - 0 degree ")
    

# %%
#* Four layers (L)+(H)+(L)+(H)

import numpy as np
import math
from matplotlib import pyplot as plt

nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi

for i in range(0,401):

    if  i < 101:
        sigmalayer = (twopi*i*1e-9*nlayerL)/lamda

        m1 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                       [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])


        b = m1[0][0] + m1[0][1]*nsub
        c = m1[1][0] + m1[1][1]*nsub 
        y = c/b

        #print(y.real)

    elif i >= 101 and i<201:
        i = i - 100
        sigmalayer = (twopi*i*1e-9*nlayerH)/lamda

        m2 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                       [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m3 = np.matmul(m2,m1)

        b = m3[0][0] + m3[0][1]*nsub
        c = m3[1][0] + m3[1][1]*nsub 
        y = c/b

    elif i >= 201 and i<301 :
        i = i - 200
        sigmalayer = (twopi*i*1e-9*nlayerL)/lamda

        m4 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                   [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m5 = np.matmul(m4,m3)

        b = m5[0][0] + m5[0][1]*nsub
        c = m5[1][0] + m5[1][1]*nsub 
        y = c/b



    elif i >= 301 and i<401:
        i = i - 300
        sigmalayer = (twopi*i*1e-9*nlayerH)/lamda

        m6 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                   [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

        m7 = np.matmul(m6,m5)


        b = m7[0][0] + m7[0][1]*nsub
        c = m7[1][0] + m7[1][1]*nsub 
        y = c/b

    plt.plot(y.real,y.imag , 'r.-')
    plt.xlabel("Real Part")
    plt.ylabel("İmaginer Part") 
    plt.title(" LHLH - B270 substrate - 0 degree")

    print(y.real, y.imag)


    


# %%
