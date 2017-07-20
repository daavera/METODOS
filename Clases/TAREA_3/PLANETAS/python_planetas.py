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
print(colors)
fig = plt.figure(figsize=(10,6))
ax = fig.gca(projection='3d')
i =0
j = 0
while(i < np.shape(datos)[1]):
	#Grafica
    x = datos[i]
    y = datos[i+1]
    z = datos[i+2]
    ax.plot(x, y, z, linewidth=0.6, label=nombres[j], color=colors[j])

    #Animacion
    # line, = ax.plot(x,y,z, 'o', linewidth=0.6)
    # def animate(i):
    #     line.set_data([0,x[i]],[0,y[i]])  # update the data
    #     line.set_3d_properties([0,z[i]])
    #     return line,
    # ani = animation.FuncAnimation(fig, animate, 100, 
    #                           interval=25)
    i+=3
    j+=1
ax.legend()
ax.set_zlabel('z')
ax.set_ylabel('y')
ax.set_xlabel('x')
plt.show()