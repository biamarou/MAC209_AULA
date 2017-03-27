import matplotlib.pyplot as plt

def metodoEuler(y0, v0, g, N):
    delta = 0.01
    for i in range (1, N + 1):
        y = y0 + v0*delta
        v = v0 - g*delta
        print (y, v)

def analitico (y0, v0, g, N):
    t = N*0.01
    y = y0 + v0 *t -1/2*g*t**2
    v = v0 - g*t

    print (y, v)


def main ():
    metodoEuler(100, 0, 9.8, 500)
    analitico(100, 0, 9.8, 500)

main()
    
