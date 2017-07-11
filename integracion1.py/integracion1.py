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

def integral_trapezoide(y):
	h = y[0]/2 + np.sum(y[1:-1]) + y[-1]/2
	w = (B-A)/(N-1)
	return(h*w)
suma_T = integral_trapezoide(funcion(x))
teorico_T = integrate.trapz(funcion(x), x)
print("Tapezoide: %f" %(suma_T))
print(teorico_T)


#Metodo de Simpson
def integral_simpson(y):
	odd = np.sum(y[1:-1:2])*4/3
	pair = np.sum(y[2:-1:2])*2/3
	h = y[0]/3 + odd + pair  + y[-1]/3
	w = (B-A)/(N-1)
	return(h*w)
suma_S = integral_simpson(funcion(x))
teorico_S = integrate.simps(funcion(x), x)
print("Simpson: %f" %(suma_S))
print(teorico_S)
