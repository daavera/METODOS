import numpy as np 
import matplotlib.pyplot as plt

#Condiciones iniciales
m = 500
g = 9.8
y0 = 0 
Vy0 = 5

t_f = 1.2
dt = 0.001
t = np.arange(0,t_f,dt)
n_points = np.size(t)
Y = np.zeros(n_points)
Vy = np.zeros(n_points)

#Segunda posicion
y1 = y0 + Vy0*dt
Vy1 = Vy0 - g*dt

#Leap-frog
def Leap_step(Y,V,i):
	V[i] = V[i-2] - g*dt*2
	Y[i] = Y[i-2] + V[i-1]*dt*2

#Evolucion
Y[0] = y0
Y[1] = y1
Vy[0] = Vy0
Vy[1] = Vy1

for i in range(2,n_points):
	Leap_step(Y,Vy,i)

print("la altura máxima alcanzada por el balón en el aire es de: %f" %(np.max(Y)))

i = 1
while(Y[i]>0):
	i+=1
print("el tiempo que el balón permanece en el aire es: %f" % (t[i]))

f1 = plt.figure(figsize=(10,6))
plt.plot(t,Y)
plt.xlabel(r"t $(s)$")
plt.ylabel(r"$y (m)$")
plt.title("Posición Vs. Tiempo")
plt.grid(True,alpha=0.5)
plt.savefig("posBalon.pdf")

f2 = plt.figure(figsize=(10,6))
plt.plot(t,Vy)
plt.xlabel(r" $t (s)$")
plt.ylabel(r"$V_y (\frac{m}{s})$")
plt.title("Velocidad Vs. Tiempo")
plt.grid(True,alpha=0.5)
plt.savefig("velBalon.pdf")






