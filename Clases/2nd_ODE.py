#ECUACIONES DIFERENCIALES 2ndo orden

import numpy as np
import matplotlib.pyplot as plt

def func_prime_1(x, y_1, y_2):
    return y_2

def func_prime_2(x, y_1, y_2):
    return -4*y_1

h=0.01
min_x = 0.0
max_x = 6.0
n_points = int((max_x-min_x)/h)
x = np.zeros(n_points)
y_1 = np.zeros(n_points)
y_2 = np.zeros(n_points)
#condiciones iniciales
x[0] = min_x
y_1[0] = 1.0
y_2[0] = 0.0

#EULER
def EulerSecondOrderStep(x_old,y_1_old,y_2_old):
	y_prime_1 = func_prime_1(x_old, y_1_old, y_2_old)
	y_prime_2 = func_prime_2(x_old, y_1_old, y_2_old)


	x_new = x_old + h
	y_1_new = y_1_old + h * func_prime_1(x_old, y_1_old, y_2_old)
	y_2_new = y_2_old + h * func_prime_2(x_old, y_1_old, y_2_old)
	return x_new, y_1_new, y_2_new

#RUNGE-KUTTA 2nd
def RungeKuttaSecondOrderStep(x_old, y_1_old, y_2_old):
	#La primera parte es para obtener los k's
	###get the first derivatives
	y_prime_1 = func_prime_1(x_old,y_1_old, y_2_old)
	y_prime_2 = func_prime_2(x_old,y_1_old, y_2_old)

	###from this estimation move to the middle point
	x_middle = x_old+ (h/2.0)
	y_1_middle = y_1_old + (h/2.0) * y_prime_1
	y_2_middle = y_2_old + (h/2.0) * y_prime_2 

	#compute the derivatives at the middle point
	y_middle_prime_1 = func_prime_1(x_middle, y_1_middle, y_2_middle)
	y_middle_prime_2 = func_prime_2(x_middle, y_1_middle, y_2_middle)

	x_new = x_old + h
	y_1_new = y_1_old + h * y_middle_prime_1 
	y_2_new= y_2_old + h * y_middle_prime_2
	return x_new, y_1_new, y_2_new

#RUNGE-KUTTA 4TH
def RungeKuttaFourthOrderStep(x_old, y1_old, y2_old):
    
	k_1_prime1 = func_prime_1(x_old,y1_old, y2_old)
	k_1_prime2 = func_prime_2(x_old,y1_old, y2_old)

	#first step
	x1 = x_old+ (h/2.0)
	y1_1 = y1_old + (h/2.0) * k_1_prime1
	y2_1 = y2_old + (h/2.0) * k_1_prime2
	k_2_prime1 = func_prime_1(x1, y1_1, y2_1)
	k_2_prime2 = func_prime_2(x1, y1_1, y2_1)

	#second step
	x2 = x_old + (h/2.0)
	y1_2 = y1_old + (h/2.0) * k_2_prime1
	y2_2 = y2_old + (h/2.0) * k_2_prime2
	k_3_prime1 = func_prime_1(x2, y1_2, y2_2)
	k_3_prime2 = func_prime_2(x2, y1_2, y2_2)


	#third
	x3 = x_old + h
	y1_3 = y1_old + h * k_3_prime1
	y2_3 = y2_old + h * k_3_prime2
	k_4_prime1 = func_prime_1(x3, y1_3, y2_3)
	k_4_prime2 = func_prime_2(x3, y1_3, y2_3)

	#fourth step
	average_k_1 = (1.0/6.0)*(k_1_prime1 + 2.0*k_2_prime1 + 2.0*k_3_prime1 + k_4_prime1)
	average_k_2 = (1.0/6.0)*(k_1_prime2 + 2.0*k_2_prime2 + 2.0*k_3_prime2 + k_4_prime2)

	x_new = x_old + h
	y_1_new = y1_old + h * average_k_1
	y_2_new= y2_old + h * average_k_2
	return x_new, y_1_new, y_2_new

y1=[[1.0,1.0,1.0]]
y2=[[0.0,0.0,0.0]]
xs=[[min_x,min_x,min_x]]

for i in range(1,n_points):
	xE,y1E,y2E = EulerSecondOrderStep(xs[i-1][0], y1[i-1][0], y2[i-1][0])
	xK2,y1K2,y2K2 = RungeKuttaSecondOrderStep(xs[i-1][1], y1[i-1][1], y2[i-1][1])
	xK4,y1K4,y2K4 = RungeKuttaFourthOrderStep(xs[i-1][2], y1[i-1][2], y2[i-1][2])

	xs.append([xE,xK2,xK4])
	y1.append([y1E,y1K2,y1K4])
	y2.append([y2E,y2K2,y1K4])

y1 =np.array(y1).T
y2 =np.array(y2).T
xs =np.array(xs).T

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(221)
ax1.plot(xs[0],y1[0])

ax2 = fig.add_subplot(222)
ax2.plot(xs[1],y1[1])

ax3 = fig.add_subplot(223)
ax3.plot(xs[2],y1[2])

plt.show()
