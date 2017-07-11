import numpy as np
import matplotlib.pyplot as plt

n_x = 160
n_t = 400
nu = 0.07
x = np.linspace(0, 2.0, n_x)
dx = x[1]-x[0]
dt = 0.001
c = 1

fig , ax = plt.subplots(2,2, figsize=(10,6))
#LINEAR CONVECTION
#but now the initial condition is not flat
u = np.ones(n_x)
u[np.where((x<1.25) & (x>0.75))] = 2.0

for n in range(n_t):  # loop over time
	u_past = u.copy() 
	for i in range(1,n_x-1): #loop over space
		u[i] = u_past[i] - c*dt/dx*(u_past[i]-u_past[i-1])
	if n%30 == 0 and n>0:
		ax[0,0].plot(x,u)
		ax[0,0].set_title("Lineal Convection")

u = np.ones(n_x)
u[np.where((x<1.25) & (x>0.75))] = 2.0
#NON LINEAL CONVECTION
for n in range(n_t):  # loop over time
	u_past = u.copy() 
	for i in range(1,n_x): #loop over space
		u[i] = u_past[i] - u_past[i]*dt/dx*(u_past[i]-u_past[i-1])
	if n%30 == 0 and n>0:
		ax[0,1].plot(x,u)
		ax[0,1].set_title("Non-lineal Convection")


#DIFUSION
n_x = 80
n_t = 100

nu = 0.3
sigma = 0.2 #sigma is a parameter to ensure \alpha\nu < 0.5

x = np.linspace(0, 2.0, n_x)
dx = x[1]-x[0]
u = np.ones(n_x)
u[np.where((x<1.25) & (x>0.75))] = 2.0
dt = sigma*dx**2/nu #dt is defined using sigma
alpha = dt/dx**2

for n in range(n_t):  # loop over time
	u_past = u.copy() 
	for i in range(1,n_x-1): #loop over space
		u[i] = nu * alpha * u_past[i+1]  + (1.0 - 2.0*nu*alpha)*u_past[i] + nu*alpha*u_past[i-1]
	if n%10 == 0 and n>0:
		ax[1,0].plot(x,u)
		ax[1,0].set_title("Difusion")

#BURGERS
n_x = 100
n_t = 700
nu = 0.07
sigma = 0.02 #sigma is a parameter to ensure \alpha\nu < 0.5
x = np.linspace(0, 2.0*np.pi, n_x)
dx = x[1]-x[0]
dt = sigma*dx**2/nu #dt is defined using sigma 
alpha = dt/dx**2
u = np.sin(x)
for n in range(n_t):
	u_past = u.copy()
	for i in range(1,n_x-1):
		u[i] = u_past[i]*(1-alpha*dx*(u_past[i]-u_past[i-1])) + nu*alpha*(u_past[i+1]-(2*u_past[i])+u_past[i-1])
	u[-1] = u_past[-1] - u_past[-1]*dt/dx*(u_past[-1]-u_past[-2]) + nu * alpha * (u_past[0] -2.0*u_past[-1]+u_past[-2])
	if n%100 == 0 and n>0:
		ax[1,1].plot(x,u)
		ax[1,1].set_title("Burgers")

plt.show() 
plt.tight_layout()
plt.close()