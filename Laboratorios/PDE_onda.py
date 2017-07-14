import numpy as np 
import matplotlib.pyplot as plt 

dt = 0.005
c=1.0
n_points = 1000
x = np.linspace(0,1,n_points)
dx = abs(x[1]-x[0])
gamma = (c*dt/dx)
u_0 = np.exp(-((x-0.3)**2)/0.01)
u_0[0] = 0
u_0[-1] = 0
u_1 = np.zeros(n_points)
for j in range(1,np.size(u_0[:-1])):
	u_1[j] = u_0[j] + ((gamma**2)/2)*(u_0[j+1]-2*u_0[j]+u_0[j-1]) 

U = []
U.append(u_0)
U.append(u_1)
U = np.array(U)
print(U[1,1])
for i in range(2,500):	
	u_new = np.zeros(n_points) 	
	for j in range(1,np.size(u_new[:-1])):
		print(U[i-2,j])
		print(U[i-1,j+1])
		print(U[i-1,j-1])
		#u_new[j] = (2*(1-gamma**2)*U[i-1,j])-U[i-2,j]+ (gamma**2*(U[i-1,j+1]+U[i-1,j-1]))
	#np.apped(U,u_new)
plt.plot(U[0])
plt.plot(U[200], alpha=0.5)
plt.show(U[400])

