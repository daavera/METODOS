import numpy as np
from scipy import integrate
#Intervalo y pasos
A  =   0.0
B  =   1
N  =   1001
x = np.linspace(A,B,N)	

#Metodo de trapezoide
def funcion(x):
	y = np.exp(x)
	return y
y = funcion(x)

def integral_trapezoide(y):
	h = y[0]/2 + np.sum(y[1:-1]) + y[-1]/2
	w = (B-A)/(N-1)
	return(h*w)
suma_T = integral_trapezoide(y)
teorico_T = integrate.trapz(y, x)
print("Tapezoide: %f" %(suma_T))
print(teorico_T)


#Metodo de Simpson
def integral_simpson(y):
	odd = np.sum(y[1:-1:2])*4/3
	pair = np.sum(y[2:-1:2])*2/3
	h = y[0]/3 + odd + pair  + y[-1]/3
	w = (B-A)/(N-1)
	return(h*w)
suma_S = integral_simpson(y)
teorico_S = integrate.simps(y, x)
print("Simpson: %f" %(suma_S))
print(teorico_S)

#Throw Monte-Carlo
def integral_Mont_T(x,y):
	n_rand = 10000
	x_rand = (np.random.rand(n_rand)*(np.max(x)-np.min(x))) + np.min(x)
	y_rand = (np.random.rand(n_rand)*(np.max(y)-np.min(y))) + np.min(y)
	delta = funcion(x_rand) - y_rand
	inside = np.where(delta>0.0)
	int_interval = (max(y)-np.min(y)) * (B-A)
	integral_T = int_interval * (np.size(inside)/np.size(y_rand)*1.0)
	return integral_T
suma_MT = integral_Mont_T(x,y)
print("Throw Montecarlo: %f" %(suma_MT))
print(teorico_S)

#Mean Monte-Carlo
def integral_Mont_M(x):
	n_rand = 10000
	x_rand = (np.random.rand(n_rand)*(np.max(x)-np.min(x))) + np.min(x)
	f_rand = funcion(x_rand)
	prom = np.sum(f_rand)/np.size(f_rand)
	integral_M = (max(x)-np.min(x))*prom
	return integral_M
suma_MM = integral_Mont_M(x)
print("Mean Montecarlo: %f" %(suma_MM))
print(teorico_S)