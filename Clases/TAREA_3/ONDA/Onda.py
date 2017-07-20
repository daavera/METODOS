import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation

n_points = 60
l = 30
c = 1
x = np.linspace(0,l,n_points)
dx = x[1]-x[0]
y = np.linspace(0,l,n_points)
dy = y[1]-y[0]
alpha = 0.5
dt = alpha*dx**2 /c
t_max = 60
t = np.arange(0,t_max,dt)
size_t = int(t_max/dt)
X, Y = np.meshgrid(x,y)
evolucion= []

def gaussian_3D (X,Y):
	A=0.5
	sigma = 0.1
	x0 = 15
	y0 = 10
	return A*np.exp(-((((X-x0)**2)/(2*sigma*2))+(((Y-x0)**2)/(2*sigma*2))))

#CONDICIONES INICIALES
phi = gaussian_3D(X,Y)
# phi = np.zeros((n_points,n_points))
# phi[int(np.size(x)/2),int(np.size(y)/3)] =1.5
bar_x = int(np.shape(phi)[1]/2)
bar_y = int(2*np.shape(phi)[1]/3)
barrera = np.arange(0,bar_x-5).tolist() + np.arange(bar_x+5,np.shape(phi)[1]).tolist()
barrera = np.array(barrera)
for i in range(np.shape(phi)[0]):
	for j in range(np.shape(phi)[1]):
		if (i==0 or i==np.shape(phi)[0]-1 or j==0 or j==np.shape(phi)[1]-1):
			phi[i,j] = 0
phi[barrera.tolist(),bar_y] = 0
evolucion.append(phi)

phi_1 = np.zeros((n_points,n_points))
for i in range(1,np.shape(phi)[0]-1):
	for j in range(1,np.shape(phi)[1]-1):
		if(np.size(np.where(barrera ==i)[0])>0 and np.size(np.where(bar_y == j)[0])>0):
			continue
		phi_1[i,j] = phi[i,j] + alpha*(phi[i+1,j]-2*phi[i,j]+phi[i-1,j])+alpha*(phi[i,j+1]-2*phi[i,j]+phi[i,j-1])
evolucion.append(phi_1)

#EVOLUCION TEMPORAL DE LA FUNCION
for k in range(2,np.size(t)):
	phi_2old = evolucion[k-2]
	phi_old = evolucion[k-1]
	phi_new = np.zeros((n_points,n_points))
	for i in range(1,np.shape(phi_old)[0]-1):
		for j in range(1,np.shape(phi_old)[1]-1):
			if(np.size(np.where(barrera ==i)[0])>0 and np.size(np.where(bar_y == j)[0])>0):
				continue
			phi_new[i,j] = (2*phi_old[i,j] - phi_2old[i,j]) + alpha*(phi_old[i+1,j]-2*phi_old[i,j]+phi_old[i-1,j])+alpha*(phi_old[i,j+1]-2*phi_old[i,j]+phi_old[i,j-1])
	evolucion.append(phi_new)
#Graficas para t30 y t60
f1 , axs = plt.subplots(1,2, figsize=(10,6))
t60 = evolucion[-1]
axs[0].pcolormesh(X,Y,t60,cmap='seismic', alpha=14)

t30 = evolucion[(int(size_t/2)-1)]
axs[1].pcolormesh(X,Y,evolucion[(int(size_t/2)-1)],cmap='seismic')
f1.savefig("Onda_ts.pdf")

f2 = plt.figure()
ax = f2.add_subplot(111, projection='3d')
ax.set_zlim(-2,2)
ax.plot_surface(X, Y, evolucion[0],rstride=1,cstride=1,cmap='summer')
def sequence(i):
    ax.clear()
    ax.set_zlim(-2,2)
    est_temp = evolucion[i]
    plt_temp = ax.plot_surface(X,Y,est_temp, rstride=1,cstride=1, cmap='summer')
    return plt_temp,
a = animation.FuncAnimation(f2,sequence,np.size(t), interval = 20, blit=False)
#a.save('Onda.mp4', writer = 'ffmpeg', fps=15)
plt.show()
plt.close()
