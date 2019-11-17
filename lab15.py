import func
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(-1.0,2.5,0.01)
y = np.tan(0.4*x+0.4)-x*x
ax.plot(x, y, 'k')
plt.title('График tg(0.4*x+0.4))=x^2')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

a = -1
b = 2.5
E = 0.001

func.table(a,b)
print()
func.dix(a,b,E)
print()
func.newton(a,b,E)
print()
func.secant(a,b,E)
print()
func.chord(a,b,E)

