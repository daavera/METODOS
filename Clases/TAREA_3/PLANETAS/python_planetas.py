import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

datos = pd.read_csv("datos_p_1.csv",header=0)

print(x2)
mpl.rcParams['legend.fontsize'] = 10


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, linewidth=0.6, label='sol', color='darkslateblue')
ax.plot(x1, y1, z1, linewidth=0.6, label='tierra', color='b')
ax.legend()
plt.show()