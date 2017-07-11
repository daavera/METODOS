
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

#Tamano del paso y num puntos
h=0.01
t_max = 40
n_points = int(t_max/h)
#Ctes
sig = 10.0
ro = 28.0
beta =8.0/3.0

t = np.linspace(0,t_max, n_points)
x = np.zeros(n_points)
y = np.zeros(n_points)
z = np.zeros(n_points)
dx = np.zeros(n_points)
dy = np.zeros(n_points)
dz = np.zeros(n_points)
#Funciones primas
def fprime_x(x,y,z):
	return sig*(y-x)
def fprime_y(x,y,z):
	return (x*(ro-z)) - y
def fprime_z(x,y,z):
	return (x*y) - (beta*z)

#Valores inicales
x[0] = 1.0
y[0] = 1.0
z[0] = 1.0
dx[0] = fprime_x(x[0],y[0],z[0])
dy[0] = fprime_y(x[0],y[0],z[0])
dz[0] = fprime_z(x[0],y[0],z[0])

#EULER
def Euler_step(x_old, dx_old):	
	x_new = h*dx_old + x_old
	return x_new

for i in range(1,n_points):
	x[i] = Euler_step(x[i-1], dx[i-1])
	y[i] = Euler_step(y[i-1],dy[i-1])
	z[i] = Euler_step(z[i-1],dz[i-1])
	dx[i] = fprime_x(x[i],y[i],z[i])
	dy[i] = fprime_y(x[i],y[i],z[i])
	dz[i] = fprime_z(x[i],y[i],z[i])

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, linewidth=0.6, label='Solucion Lorenz', color='darkslateblue')
ax.legend()
plt.savefig('lorenz.png')