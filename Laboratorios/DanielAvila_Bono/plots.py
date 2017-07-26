import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint

#Leer los datos
datos = pd.read_csv("data.csv", header=None)

#Separar los datos
x = datos.iloc[1:,0].values
t = datos.iloc[0,1:].values
u = datos.iloc[1:,1:]

#Generacion random de colores
colors = []
for i in range(10):
    colors.append('#%06X' % randint(0, 0xFFFFFF))

i = 0
j=0
fig = plt.figure(figsize=(10,6))
while(i<np.size(t)):
    plt.plot(x,u.iloc[:,i], label=r"$t= $ %f" %(t[i]), color=colors[j])
    i += 59
    j +=1
plt.legend()
plt.title("Convección lineal", fontsize=15)
plt.xlabel(r"$0<x<2$", fontsize=12)
plt.ylabel(r"$u\,(x,t)$", fontsize=12)
plt.grid(True, alpha=0.4)
plt.savefig("grafica_conveccion.png")
#plt.show()