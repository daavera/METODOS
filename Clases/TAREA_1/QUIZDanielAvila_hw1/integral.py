import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sin(x)

x = np.linspace(0,np.pi,1000)
y = f(x)

n_random = 10000

def integral(x,y,n_random):
	y_rand = (np.random.rand(n_random) * (np.max(y)-np.min(y))) + np.min(y)
	x_rand = (np.random.rand(n_random) * (np.max(x)-np.min(x))) + np.min(x)
	delta = f(x_rand) - y_rand
	int_interval = (np.max(y)-np.min(y)) * (np.max(x)-np.min(x))
	integral = int_interval * np.size(np.where(delta>0))/np.size(y_rand)*1.0
	return integral

prom_int=[]
for i in range(20):
	prom_int.append(integral(x,y,n_random))
prom_int = np.array(prom_int)
prom_int = np.sum(prom_int)/np.size(prom_int)

print('El valor de la integral es %f' %(prom_int))
