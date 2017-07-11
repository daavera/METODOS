#CALCULO DE PI

import numpy as np 
import matplotlib.pyplot as plt


a = 0
b = 2
N = 1001
h = abs(b-a)/(N-1)
x = np.linspace(a,b,N)

def f_circulo(x):
	#realmente es medio circulo
	#y = np.sin(np.arccos(x))
	y = np.sqrt(1-x**2)
	return y

def trapezoide(y,h):
	int_t = np.sum(y[1:-1])+((y[0]+y[-1])*1/2)
	return int_t*h

def simpson(y,h):
	pair = np.sum(y[1:-1:2])*4/3
	odd = np.sum(y[2:-1:2])*2/3
	int_s = ((y[0]+y[-1])*1/2) + odd + pair
	return int_s*h

def montecarlo(y,h):
	n_rand = 10000000
	x_rand = (np.random.rand(n_rand) * np.max(x)-np.min(x)) + np.min(x)
	y_rand = (np.random.rand(n_rand) * np.max(y)-np.min(y)) + np.min(y)
	delta = f_circulo(x_rand)-y_rand
	i = np.where(delta>0.0)
	int_interval = (np.max(x)-np.min(x)) * (np.max(y)-np.min(y))
	int_m = int_interval* np.size(i)/np.size(y_rand)
	return int_m
y = f_circulo(x)
print(trapezoide(y,h)*4,simpson(y,h)*4,montecarlo(y,h)*4)
