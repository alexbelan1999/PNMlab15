import numpy as np
import math

def tg(x):
    return np.tan(0.4*x+0.4)-x*x
    #return x*x*x - 3*x-0.4

def table(a,b):
    x = []
    y = []
    print("Таблица")
    for i in range(a,b+1):
        x.append(i)
        y.append(tg(i))
    print("x:",x)
    print("y:", y)
    pass

def dix(a,b,E):
    iter = 0
    print("Метод дихотамии")

    while ((b - a) / 2 >= E):
        c = (a + b) / 2
        fa = math.copysign(1, tg(a))
        fc = math.copysign(1, tg(c))

        print(a, "  ", b, "  ", c, "  ", tg(c))
        if (fa != fc):
            b = c
        else:
            a = c
        iter += 1

    print("Корень X*= ", c," с точностью ",E," количество итераций ",iter)
    pass