import matplotlib.pyplot as plt
import math as th

def shoAnalytical (n, k, m):
    # A = y(t = 0), B = v(t = 0)/w0
    
    A = 100
    B = 0
    w0 = th.sqrt(k/m)
    
    for i in range (0, n, 1):
        ds = A * th.cos(w0 * i) + B * th.sin(w0 * i)
        plt.plot(i, ds, 'yo')

def shoEuler (n, k, m):

    A = 100
    B = 0 
    w0 = th.sqrt(k/m)
    ds = 0
    
    for i in range (0, n, 1):
        ds = ds + (A * (-th.sin(w0 * i)) * w0) + (B * th.cos(w0 * i) * w0)
        plt.plot(i, ds, 'ro')

def shoEulerLivro (v0, x0, n):

    v = v0
    x = x0
    k = 2
        
    for dt in range (0, n, 1):
        v = v - k * x * dt
        x = x + v * dt
        plt.plot (dt, x, 'go')
    
    
def main ():
    shoAnalytical (1000, 2, 10)
    shoEuler (1000, 2,  10)
    shoEulerLivro (0, 100, 1000)
    plt.show()

main()
