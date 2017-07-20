import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

datos = pd.read_csv("datos_planetas.csv",header=0)

x = datos['X']
y = datos['Y']
z = datos['Z']
x2 = datos['X2']
y2 = datos['Y2']
z2 = datos['Z2']

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x, y, z, linewidth=0.6, label='sol', color='darkslateblue')
ax.scatter(x2, y2, z2, linewidth=0.6, label='tierra', color='b')
ax.legend()
plt.show()