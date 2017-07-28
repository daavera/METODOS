import numpy as np
import matplotlib.pyplot as plt

#DATOS
data = np.loadtxt("map_data.txt")

n_row , n_col = np.shape(data)

results = np.loadtxt("results.txt")

#COORDENADAS
coord_lat = results[1]
coord_long = results[0]
r_nemo = results[2]


def circulo(xC,yC,r):
    t = np.linspace(0,2*np.pi,1000)
    x = r*np.cos(t) + xC
    y = r*np.sin(t) + yC
    return x,y
x,y = circulo(coord_lat,coord_long,r_nemo)


fig, ax = plt.subplots(1,1,figsize=(10,6))
#MAPA
ax.imshow(data, cmap="YlGn")
#PUNTO NEMO
ax.scatter(coord_lat,coord_long, color="crimson", edgecolor='black')
#CIRCULO MAXIMO
ax.fill_between(x, y, facecolor='crimson', interpolate=True, alpha=0.3)
ax.set_ylabel("Latitud")
ax.set_xlabel("Longitud")
ax.set_title("Punto Nemo", fontsize=15)

ax.set_xticks(np.linspace(0, n_col, 7))
ax.set_yticks(np.linspace(n_row, 0, 7))
x_l =["-180°","-120°","-60°","0°","60°","120°","180°"]
y_l =["-90°","-60°","-30°","0°","30°","60°","90°"]

ax.set_xticklabels(x_l)
ax.set_yticklabels(y_l)
plt.savefig("PuntoNemo.pdf")
