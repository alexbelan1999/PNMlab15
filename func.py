import numpy as np
import math

def tg(x):
    return np.tan(0.4*x+0.4)-x*x
    #return x*x*x - 3*x-0.4

def deriv1(x):
    return -2*x + 0.4/(math.cos(0.4*x+0.4)*math.cos(0.4*x+0.4))

def deriv2(x):
    return 0.32*math.sin(0.4*x+0.4)/pow(math.cos(0.4*x+0.4),3) - 2

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

    print("Корень = ", c," с точностью ",E," количество итераций ",iter)
    pass

def newton(a,b,E):
    print("Метод Ньютона")
    iter = 0
    x0 = 0
    xn = 0
    if (tg(a) * deriv2(a) != 0):
        x0 = a
    else :
        x0 = b
    while (abs(tg(x0) / deriv1(x0)) > E):
        xn = x0 - tg(x0) / deriv1(x0)
        print(x0, tg(x0), deriv1(x0), xn)
        x0 = xn
        iter += 1
    print("Корень = ", xn, " с точностью ", E, " количество итераций ", iter)
    pass
