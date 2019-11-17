import numpy as np
import math

def tg(x):
    return math.tan(0.4*x+0.4)-x*x
    #return x*x*x - 3*x-0.4

def deriv1(x):
    return -2 * x + 0.4 / (math.cos(0.4 * x + 0.4) * math.cos(0.4 * x + 0.4))

def deriv2(x):
    return 0.32 * math.sin(0.4 * x + 0.4) / pow(math.cos(0.4 * x + 0.4), 3) - 2

def table(a,b):
    x = []
    y = []
    print("Таблица")
    for i in np.arange(a,b+0.25,0.25):
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
        fa = tg(a)
        fc = tg(c)

        print(a, "  ", b, "  ", c, "  ", fc)
        if (fc < 0 and fa < 0) or (fc > 0 and fa > 0):
            a = c
        else:
            b = c
        iter += 1

    print("Корень = ", c," с точностью ",E," количество итераций ",iter)
    pass

def newton(a,b,E):
    print("Метод Ньютона")
    iter = 0
    x = a
    x1 = x - tg(x) / deriv1(x)
    while (abs(x1 - x) >= E) :
        x = x1
        x1 = x1 - tg(x1) / deriv1(x1)
        print(x, "  ", x1, "  ", tg(x), "  ", deriv1(x))
        iter += 1
    print("Корень = ", x1, " с точностью ", E, " количество итераций ", iter)
    pass

def secant(a,b,E):
    print("Метод секущих")
    iter = 0
    x = a
    x_1 = b
    x1 = x - tg(x) / ((tg(x)-tg(x_1))/(x-x_1))
    while (abs(x1 - x) >= E) :
        x_1 = x
        x = x1
        x1 = x1 - tg(x1) / ((tg(x)-tg(x_1))/(x-x_1))
        print(x_1, "  ", x, "  ", x1, "  ", tg(x), "  ", tg(x_1))
        iter += 1
    print("Корень = ", x1, " с точностью ", E, " количество итераций ", iter)

    pass

def chord(a,b,E):
    print("Метод секущих")
    iter = 0
    x = a
    x0 = a + E
    x1 = x - tg(x) / ((tg(x) - tg(x0)) / (x - x0))
    while (abs(x1 - x) >= E):
        x = x1
        x1 = x1 - tg(x1) / ((tg(x) - tg(x0)) / (x - x0))
        print(x0, "  ", x, "  ", x1, "  ", tg(x), "  ", tg(x0))
        iter += 1
    print("Корень = ", x1, " с точностью ", E, " количество итераций ", iter)

    pass
