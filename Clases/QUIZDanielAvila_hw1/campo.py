import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('pot.dat')
x = datos[:,0]
pot = datos[:,1]
h_x = abs(x[1]-x[0])

d = pot[2:]-pot[:-2]/(2*h_x)
E = -d

plt.scatter(x[1:-1],E)
plt.ylabel(r'$\vec{E}$')
plt.xlabel('Posición')
plt.title('Campo eléctrico VS. Posición')
plt.grid(True)
plt.savefig('campo.pdf')