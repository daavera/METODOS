import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

g=9.8
l = 0.4

h = 0.01
n_points = 1000

gamma_crit = 9.899
gamma_sub = 0.2
gamma_sob = 11

t = np.zeros(n_points)
theta_1 = np.zeros(n_points)
theta_2 = np.zeros(n_points)

def func_theta_1(t,theta_1,theta_2):
	return theta_2

def func_theta_2(t,gamma,theta_1,theta_2):
	return -(g/l)*np.sin(theta_1)-(gamma*theta_2)

#cond. iniciales
theta_1[0]= -np.pi
theta_2[0] = 0.5 

def RungeKuttaStep (t_old, gamma,theta1_old, theta2_old):
	k_1_prime1 = func_theta_1(t_old,theta1_old,theta2_old)
	k_1_prime2 = func_theta_2(t_old,gamma,theta1_old,theta2_old)

	t1 = t_old + (h/2.0)
	T1_1 = theta1_old + (h/2.0) * k_1_prime1
	T2_1 = theta2_old + (h/2.0) * k_1_prime2
	k_2_prime1 = func_theta_1(t1, T1_1, T2_1)
	k_2_prime2 = func_theta_2(t1, gamma,T1_1, T2_1)

	#second step
	t2 = t_old + (h/2.0)
	theta1_2 = theta1_old + (h/2.0) * k_2_prime1
	theta2_2 = theta2_old + (h/2.0) * k_2_prime2
	k_3_prime1 = func_theta_1(t2, theta1_2, theta2_2)
	k_3_prime2 = func_theta_2(t2, gamma,theta1_2, theta2_2)


	#third
	t3 = t_old + h
	theta1_3 = theta1_old + h * k_3_prime1
	theta2_3 = theta2_old + h * k_3_prime2
	k_4_prime1 = func_theta_1(t3, theta1_3, theta2_3)
	k_4_prime2 = func_theta_2(t3, gamma,theta1_3, theta2_3)

	#fourth step
	average_k_1 = (1.0/6.0)*(k_1_prime1 + 2.0*k_2_prime1 + 2.0*k_3_prime1 + k_4_prime1)
	average_k_2 = (1.0/6.0)*(k_1_prime2 + 2.0*k_2_prime2 + 2.0*k_3_prime2 + k_4_prime2)

	t_new = t_old + h
	theta_1_new = theta1_old + h * average_k_1
	theta_2_new= theta2_old + h * average_k_2
	return t_new,theta_1_new,theta_2_new

for i in range(1,n_points):
	t[i],theta_1[i],theta_2[i] = RungeKuttaStep(t[i-1],gamma_sub,theta_1[i-1],theta_2[i-1])

x = l*np.sin(theta_1)
y = l*np.cos(theta_1)

fig, ax1 = plt.subplots()
line, = ax1.plot(x,-y, '-o')
def animate(i):
    line.set_data([0,x[i]],[0,-y[i]])  # update the data
    return line,

ani = animation.FuncAnimation(fig, animate, n_points, 
                              interval=25)
ax1.set_ylim(-1,1)
ax1.set_xlim(-1,1)
plt.show()