import matplotlib.pyplot as plt
import numpy as np

def metodoEuler(y0, v0, g, N):
   
    for i in np.arange (0, N, 0.1):
        y = y0 + v0*i
        v = v0 - g*i
        plt.plot(i,y,'ro')

def analitico (y0, v0, g, N):

    for t in np.arange (0, N, 0.1):
        y = y0 + v0 *t -1/2*g*t**2
        v = v0 - g*t
        plt.plot(t,y,'yo')

def main ():
    metodoEuler(100, 0, 9.8, 500)
    analitico(100, 0, 9.8, 500)
    plt.show()
main()
    
