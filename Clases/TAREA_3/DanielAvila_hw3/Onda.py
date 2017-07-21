import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation

n_points = 300
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
bar_x = int(np.shape(phi)[1]/2)
bar_y = int(2*np.shape(phi)[1]/3)
ancho = int(n_points/25)
barrera = np.arange(0,bar_x-ancho).tolist() + np.arange(bar_x+ancho,np.shape(phi)[1]).tolist()
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

#GRAFICAS PARA T30 & T60
#t30
f1 = plt.figure(figsize=(10,6))
t30 = evolucion[(int(size_t/2)-1)]
t30[barrera.tolist(),bar_y] = np.nan
plt.pcolormesh(X,Y,t30,cmap='summer', vmin=-0.03, vmax=0.03)
bar = plt.colorbar()
bar.set_label(r'Amplitud', rotation=270, fontsize= 7.5)
plt.xlabel('x', fontsize=11)
plt.ylabel('y', fontsize=11)
plt.title(r"Propagación de la Onda para $t_{30}$", fontsize=15)
f1.tight_layout()
f1.savefig("grafica_o_1.png")

#t60
f2 = plt.figure(figsize=(10,6))
t60 = evolucion[-1]
t60[barrera.tolist(),bar_y] = np.nan
plt.pcolormesh(X,Y,t60,cmap='summer', vmin=-0.03, vmax=0.03)
bar = plt.colorbar()
bar.set_label(r'Amplitud', rotation=270, fontsize= 7.5)
plt.xlabel('x', fontsize=11)
plt.ylabel('y', fontsize=11)
plt.title(r"Propagación de la Onda para $t_{60}$",fontsize= 15)
f2.tight_layout()
f2.savefig("grafica_o_2.png")

#ANIMACION
f3 = plt.figure()
ax = f3.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, evolucion[0],rstride=1,cstride=1,cmap='summer')
def sequence(i):
	ax.clear()
	ax.set_xlabel('x', fontsize=12)
	ax.set_ylabel('y', fontsize=12)
	ax.set_zlabel('Amplitud', fontsize=12)
	ax.set_title(r"Evolución temporal de la función de Onda")
	ax.set_zlim(-2,2)
	est_temp = evolucion[i]
	plt_temp = ax.plot_surface(X,Y,est_temp, rstride=1,cstride=1, cmap='summer')
	return plt_temp,
a = animation.FuncAnimation(f3,sequence,np.size(t), interval = 10, blit=False)
a.save('Onda.mp4', writer = 'ffmpeg', fps=int(size_t/45))

