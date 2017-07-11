import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation


g = 9.8
k = 42.0
mu = 0.15
m = 0.25

h = 0.001
min_t = 0
max_t = 5
n_points = int((max_t - min_t)/h)

t = np.zeros(n_points)
x = np.zeros(n_points)
dx = np.zeros(n_points)

x[0] = 0.2
dx[0] = 0.0

def func_prime_1(t,x,dx):
	return dx
def func_prime_2(t,x,dx):
	if(dx >= 0):	
		d2 = (-k/m)*x-(mu*g)
	else:
		d2 = (-k/m)*x+(mu*g)
	return d2


def Euler_step(t0,x0,dx0):
	t_new = t0 +h 
	x_new = func_prime_1(t0,x0,dx0)*h + x0
	dx_new = func_prime_2(t0,x0,dx0)*h + func_prime_1(t0,x0,dx0)
	return t_new, x_new, dx_new

for i in range(1,n_points):
	t[i], x[i], dx[i] = Euler_step(t[i-1],x[i-1],dx[i-1])

fig, ax1 = plt.subplots()
plt.plot(t,x, linestyle='--', alpha=0.3)
line, = ax1.plot(t,x, '-o')
def animate(i):
    line.set_data(t[i],x[i])  # update the data
    return line,

ani = animation.FuncAnimation(fig, animate, n_points, 
                              interval=1)
plt.show()