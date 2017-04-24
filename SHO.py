import matplotlib.pyplot as plt
import math as th
import numpy as np

def shoAnalytical (n, k, m):
    # A = y(t = 0), B = v(t = 0)/w0

    list_t = []
    list_ds = []
    
    A = 100
    B = 0
    w0 = th.sqrt(k/m)

        
    for t in np.arange (0,n,0.1):
        ds = A * th.cos(t) + B * th.sin(t)
        list_ds.append(ds)
        list_t.append(t)
        
    plt.plot(list_t, list_ds)

def shoEulerLivro (v0, x0, n):

    list_dt = []
    list_x = []

    v = v0
    x = x0
    k = 1
    t = 0
    dt = 0.1    

    for i in np.arange (0,n,0.1):
       
        v = v - k * x * dt
        x = x + v * dt
        t = t + dt
        list_dt.append(t)
        list_x.append(x)

    plt.plot(list_dt, list_x)
    
def main ():
    shoAnalytical (1000, 2, 10)
    shoEulerLivro (0, 100, 1000)
    plt.show()

main()
