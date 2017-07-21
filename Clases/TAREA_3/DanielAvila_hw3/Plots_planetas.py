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
while(i < np.shape(datos)[1]):
	#Grafica
    x = datos[i]
    y = datos[i+1]
    z = datos[i+2]
    ax.plot(x, y, z, linewidth=0.6, color=colors[j], label=nombres[j])

    #Animacion
    point, = ax.plot([x[0]],[y[0]],[z[0]], 'o', linewidth=0.6,color=colors[j])
    def step(i,x,y,z,point):
        point.set_data(np.array([x[i],y[i]]))  # update the data
        point.set_3d_properties(z[i], 'z')
        return point,
    ani = animation.FuncAnimation(fig, step, interval = 1, fargs=(x,y,z,point),blit=False)
    i+=3
    j+=1


ax.set_zlabel(r'$z (UA)$')
ax.set_ylabel(r'$y (UA)$')
ax.set_xlabel(r'$x (UA)$')
lgd = ax.legend(numpoints=1)
ax.set_title("Orbitas el sistema solar", fontweight='bold')
plt.savefig('grafica_p_1.png',bbox_extra_artists=(lgd,), bbox_inches='tight')
