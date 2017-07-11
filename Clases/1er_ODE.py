#ECUACIONES DIFERENCIALES 1er orden

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))


def func_prime(x,y):
    return -y
##EULER
ax1 = fig.add_subplot(221)
h=0.01
min_x = 0.0
max_x = 4.0
n_points = int((max_x - min_x)/h)
x_e = np.zeros(n_points)
y_e = np.zeros(n_points)

x_e[0] = min_x
y_e[0] = 1.0
for i in range(1,n_points):
	x_e[i] = x_e[i-1] + h
	y_e[i] = y_e[i-1] + h * func_prime(x_e[i-1],y_e[i-1])
ax1.plot(x_e,y_e, 'ko')
ax1.plot(x_e,np.exp(-x_e))
ax1.set_xlabel('x')
ax1.set_ylabel('y(x)')


#LEAP-FROG
ax2 = fig.add_subplot(222)
x_l = np.zeros(n_points)
y_l = np.zeros(n_points)
x_l[0] = min_x
y_l[0] = 1.0

x_l[1] = min_x + h
y_l[1] = y_l[0] + h*func_prime(x_l[0],y_l[0])

for i in range(2,n_points):
    x_l[i] = x_l[i-1] + h
    y_l[i] = y_l[i-2] + 2 * h * func_prime(x_l[i-1],y_l[i-1])

ax2.plot(x_l,y_l, 'ko')
ax2.plot(x_l,np.exp(-x_l))
ax2.set_xlabel('x')
ax2.set_ylabel('y(x)')

#RUNGE-KUTTA 2ND
ax3 = fig.add_subplot(223)
h=0.01
min_x = 0.0
max_x = 4.0
n_points = int((max_x - min_x)/h)
x_K2 = np.zeros(n_points)
y_k2 = np.zeros(n_points)

x_K2[0] = min_x
y_k2[0] = 1.0
for i in range(1,n_points):
    k1 = h * func_prime(x_K2[i-1], y_k2[i-1])
    k2 = h * func_prime(x_K2[i-1] + 0.5 * h, y_k2[i-1] + 0.5 * k1)
    x_K2[i] = x_K2[i-1] + h
    y_k2[i] = y_k2[i-1] + k2
ax3.plot(x_K2,y_k2, 'ko')
ax3.plot(x_K2,np.exp(-x_K2))
ax3.set_xlabel('x')
ax3.set_ylabel('y(x)')

#RUNGE-KUTTA 4TH
ax4 = fig.add_subplot(224)
h=0.01
min_x = 0.0
max_x = 4.0
n_points = int((max_x - min_x)/h)
x_K4 = np.zeros(n_points)
y_k4 = np.zeros(n_points)
x_K4[0] = min_x
y_k4[0] = 1.0
for i in range(1,n_points):
    k1 = h * func_prime(x_K4[i-1]          , y_k4[i-1])
    k2 = h * func_prime(x_K4[i-1] + 0.5 * h, y_k4[i-1] + 0.5 * k1)
    k3 = h * func_prime(x_K4[i-1] + 0.5 * h, y_k4[i-1] + 0.5 * k2)
    k4 = h * func_prime(x_K4[i-1] + h      , y_k4[i-1] + k3)
    
    #fourth step
    average_k = (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
    
    x_K4[i] = x_K4[i-1] + h
    y_k4[i] = y_k4[i-1] + average_k
ax4.plot(x_K4,y_k4, 'ko')
ax4.plot(x_K4,np.exp(-x_K4))
ax4.set_xlabel('x')
ax4.set_ylabel('y(x)')

plt.show()
