import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("datos.txt")

t = datos[:,0]
N = datos[:,1]
N_stc = datos[:,2]
N_prom = datos[:,3]

plt.plot(t,N)
plt.plot(t,N_stc)
plt.plot(t,N_prom)
plt.show()