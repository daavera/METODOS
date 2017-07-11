import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('bmh')

datos = pd.read_csv('food-texture.csv', sep=',')
datos = datos.ix[:,1:]
datos = (datos-datos.mean(axis=0))/datos.std(axis=0)

cov = np.cov(datos.T)
values , vectors = np.linalg.eig(cov)
percent = []

for val in values:
	percent.append((val*100)/np.sum(values))

fig, ax = plt.subplots(2,1, figsize=(6,6))

ax[0].scatter(datos.ix[:,0],datos.ix[:,3])
v1 = vectors[0,:2]
v2 = vectors[3,:2]
ax[0].plot([v1[0],-v1[0]], [v2[0] ,-v2[0]], marker = 'o', color='r')
ax[0].plot([v1[1],-v1[1]], [v2[1] ,-v2[1]], marker = 'o', color='g')
ax[0].grid(True)

ax[1].scatter(datos.ix[:,0],datos.ix[:,2])
V1 = vectors[0,:2]
V2 = vectors[2,:2]
ax[1].plot([V1[0],-V1[0]], [V2[0] ,-V2[0]], marker = 'o', color='r')
ax[1].plot([V1[1],-V1[1]], [V2[1] ,-V2[1]], marker = 'o', color='g')
ax[1].grid(True)

plt.show()
plt.close()

datos.columns()

