import numpy as np
import matplotlib.pyplot as plt

N = 200
f = 200
dt = 1/(f*50)
t = np.linspace(0, (N-1)*dt,N)
y = np.cos(2*np.pi*f*t)

#plt.plot(t,y)
#plt.plot(t,y,'ko')
#plt.xlabel('time(s)')
#plt.ylabel('y(t)')
#plt.show()



def G (y,N):
	n = np.arange(0,N,1)
	w = n/1.0*N
	G=[]
	for w_0 in w:
		G_0 = 0
		for k in n:
			G_0 += y[k]*np.exp(-2*np.pi*1j*t[k]*w_0)
		G.append(G_0)
	G = np.array(G)
	return G,n
G,n = G(y,N)
print(G)
plt.plot(n,G*(n/N))
plt.show()




			


