import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

datos = pd.read_csv('room-temperature.csv', sep=',')
datos = datos.ix[:,1:]

#Temperatura en cada esquina
f1, ax = plt.subplots(2,2, figsize=(6,6))
ax[0,0].plot(datos['FrontLeft'])
ax[0,0].set_title('Front Left')

ax[0,1].plot(datos['FrontRight'], c='g')
ax[0,1].set_title('Front Right')

ax[1,0].plot(datos['BackLeft'],c='r')
ax[1,0].set_title('Back Left')

ax[1,1].plot(datos['BackRight'], c='y')
ax[1,1].set_title('Back Right')

plt.tight_layout()
plt.savefig('temp.png')

#Matriz de Covarianza
datos_norm = (datos-datos.mean(axis=0))/datos.std(axis=0)
cov = np.cov(datos_norm.T)

#Autovectores y autovalores
values , vectors = np.linalg.eig(cov)
orden = ["primera","segunda","tercera","cuarta"]
for i in range(2):
	print('La %s componente principal es %s con valor %f.' % (orden[i],vectors[:,i],values[i]))

print('\n')

for i in range(2):
	per = (values[i]*100)/np.sum(values)
	print('La %s componente principal explica el %f porciento de la varianza.' %(orden[i],per))

#Component analisis (graficos)
f2 = plt.figure(figsize=(10,6))
plt.scatter(datos_norm['FrontRight'],datos_norm['FrontLeft'], c='purple', label ='Datos')
v1 = vectors[0,:2]
v2 = vectors[1,:2]
plt.plot(2.5*np.array([v1[0],-v1[0]]),2.5*np.array([v2[0],-v2[0]]),marker = 'o', color='greenyellow',label='PCA1')
plt.plot(2.5*np.array([v1[1],-v1[1]]),2.5*np.array([v2[1],-v2[1]]),marker = 'o', color='orange',label='PCA2')
plt.title('Front Right vs. Front Left')
plt.xlabel('Front Left')
plt.ylabel('Front Right')
plt.legend(loc='upper left')
plt.savefig('pca_fr_fl.pdf')

f3 = plt.figure(figsize=(10,6))
plt.scatter(datos_norm['BackLeft'],datos_norm['FrontLeft'], c='brown', label='Datos')
V1 = vectors[0,:2]
V2 = vectors[2,:2]
plt.plot(2.5*np.array([V1[0],-V1[0]]), 2.5*np.array([V2[0] ,-V2[0]]), marker = 'o', color='greenyellow',label='PCA1')
plt.plot(2.5*np.array([V1[1],-V1[1]]), 2.5*np.array([V2[1] ,-V2[1]]), marker = 'o', color='orange', label='PCA2')
plt.title('Back Left vs Front Left')
plt.legend(loc='upper left')
plt.xlabel('Front Left')
plt.ylabel('Back Left')
plt.savefig('pca_bl_fl.pdf')