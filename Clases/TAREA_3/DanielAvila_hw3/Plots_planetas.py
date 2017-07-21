import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from random import randint
import matplotlib.animation as animation

datos = pd.read_csv("datos_p_1.csv", header=None)

colors = ['#FFFF00','#708090','#FFFFE0','#00FF7F','#B22222','#E9967A','#D2B48C','#20B2AA','#708090','#2F4F4F']
nombres = ['Sol','Mercurio','Venus','Tierra','Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno', 'Plutón']
fig = plt.figure(figsize=(10,6))
ax = fig.gca(projection='3d')
i =0
j = 0

X = []
Y = []
Z = []

while(i < np.shape(datos)[1]):
	#Grafica
    x = datos[i]
    y = datos[i+1]
    z = datos[i+2]
    X.append(x)
    Y.append(y)
    Z.append(z)
    ax.plot(x, y, z, linewidth=0.6, color=colors[j], label=nombres[j])

    #Animacion
    i+=3
    j+=1
X = np.array(X[0][:])
Y = np.array(Y)
Z = np.array(Z)
print(X)
point, = ax.plot([X[0,:]],[Y[0,:]],[Z[0,:]], 'o', linewidth=0.6,color=colors[j])
def step(i,X,Y,Z,point):
    point.set_data(np.array(X[i,:],Y[i,:]))  # update the data
    point.set_3d_properties(Z[i,:], 'Z')
    return point,
ani = animation.FuncAnimation(fig, step, np.shape(datos)[0],interval = 1, fargs=(X,Y,Z,point),blit=False)

ax.set_zlabel(r'$z (UA)$')
ax.set_ylabel(r'$y (UA)$')
ax.set_xlabel(r'$x (UA)$')
lgd = ax.legend(numpoints=1)
ax.set_title("Orbitas el sistema solar", fontweight='bold')
plt.savefig('grafica_p_1.png',bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.show()