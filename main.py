import numpy as np
import matplotlib.pyplot as plt



#From the data in the following table, find the value
#of P(50) by using Lagrange interpolation

x = np.array([8.1, 8.3, 8.6, 8.7], float)
y = np.array([16.94410, 17.56492, 18.50515, 18.82091], float)

inp = input("Enter x: ")
if inp == '':
    xplt = np.linspace(x[0], x[-1])
    yplt = np.array([], float)

    for xp in xplt:
        yp = 0

        for xi, yi in zip(x, y):
            yp += yi * np.prod((xp - x[x != xi])/(xi - x[x != xi]))
        yplt = np.append(yplt, yp)

    #plot
    plt.plot(x, y, 'ro', xplt, yplt, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
else:
    xp = float(inp)
    yp = 0

    for xi, yi in zip(x, y):
        yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi]))

    print('For x = %.2f, y = %f' % (xp, yp))








