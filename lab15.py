import func
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(-2.0,2.0,0.01)
y = np.tan(0.4*x+0.4)-x*x
ax.plot(x, y, 'k')
plt.title('График tg(0.4*x+0.4))=x^2')
plt.grid(True)
plt.show()

a = -2
b = 2
E = 0.001

func.table(a,b)
print()
func.dix(a,b,E)
print()
func.newton(a,b,E)


