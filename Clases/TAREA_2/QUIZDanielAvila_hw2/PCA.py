import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("room-temperature.csv", delimiter=",",skip_header=1, usecols=(1,2,3,4))
for j in range(np.shape(datos)[1]):
	datos[:,j] = (datos[:,j]-np.mean(datos[:,j]))/np.std(datos[:,j])

cov = np.cov(datos.T)
val , vec = np.linalg.eig(cov)
print("PC1 es: %s y PC2 es %s" %(vec[:,0],vec[:,1]))

fig = plt.figure(figsize=(10,6))
num_vec= np.size(val)
plt.grid(True, alpha=0.6)
for i in range(num_vec):
	label = "T" + str(i+1)
	plt.scatter(vec[i,0],vec[i,1], label=label, s=150, alpha=0.6)
plt.legend()
plt.title("Agrupacion de variables")
plt.xlim(-0.8,-0.2)
plt.savefig("Agrupaciones.pdf")
	


