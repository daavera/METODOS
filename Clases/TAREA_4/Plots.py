import numpy as np
import matplotlib.pyplot as plt

#DATOS
data = np.loadtxt("map_data.txt")

#COORDENADAS
coord_x = 150
coord_y = 300

def circulo(xC,yC,r):
    t = np.linspace(0,2*np.pi,1000)
    x = r*np.cos(t) + xC
    y = r*np.sin(t) + yC
    return x,y
x,y = circulo(coord_x,coord_y,100)

#MAPA
plt.imshow(data)
#PUNTO NEMO
plt.scatter(coord_x,coord_y)
#CIRCULO MAXIMO
plt.plot(x,y)
plt.show()