#METROPOLIS-HASTING

import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-4.0,4.0,1000)
def nasty_function(x):
    x_0 = 3.0
    a = 0.01
    return 10.*np.exp(-(x**2))/((x-x_0)**2 + a**2)

x_walk = []
x_0 = 8.0*(np.random.random()-0.5)
x_walk.append(x_0)

n_iterations = 50000
for i in range(n_iterations):
	x_prime = np.random.normal(x_walk[i], 0.1) #0.1 is the sigma (std. dev) in the normal distribution

	if(x_prime>4.0 or x_prime<-4.0):
		continue
	alpha = nasty_function(x_prime)/nasty_function(x_walk[i])
	if(alpha >= 1.0):
		x_walk = np.append(x_walk,x_prime)
	else:
		beta = np.random.random()
		if(beta<=alpha):
			x_walk = np.append(x_walk,x_prime)
		else:
			x_walk = np.append(x_walk,x_walk[i])

f = nasty_function(x)
norm = sum(f*(x[1]-x[0]))
plt.plot(x,f/norm, linewidth=1, color='r')
count, bins, ignored = plt.hist(x_walk, 1000, normed=True)
plt.show()
