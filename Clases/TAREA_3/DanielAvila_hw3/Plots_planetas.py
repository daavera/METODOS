import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from random import randint
import matplotlib.animation as animation

datos = pd.read_csv("datos_p_1.csv", header=None)
datos = datos[::1000]
colors = ['#FFFF00','#708090','#FFFFE0','#00FF7F','#B22222','#E9967A','#D2B48C','#20B2AA','#708090','#2F4F4F']
nombres = ['Sol','Mercurio','Venus','Tierra','Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno', 'Plutón']
fig = plt.figure(figsize=(10,6))
ax = fig.gca(projection='3d')
i =0
j = 0
X =[]
Y =[]
Z = []
points = []
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
    point, = ax.plot([],[],[], 'o', linewidth=0.6,color=colors[j])
    points.append(point)
    i+=3
    j+=1

def step(i,x,y,z,point):
    for j, p in enumerate(points):
        p.set_data(np.array([X[j][i],Y[j][i]]))  # update the data
        p.set_3d_properties(Z[j][i], 'z')
        return p,

ani = animation.FuncAnimation(fig, step, np.shape(datos)[0] ,interval = 1, fargs=(x,y,z,point),blit=False)
plt.show()

ax.set_zlabel(r'$z (UA)$')
ax.set_ylabel(r'$y (UA)$')
ax.set_xlabel(r'$x (UA)$')
lgd = ax.legend(numpoints=1)
ax.set_title("Orbitas el sistema solar", fontweight='bold')
plt.savefig('grafica_p_1.png',bbox_extra_artists=(lgd,), bbox_inches='tight')
