import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.style.use('seaborn-white')

#CARGA
class Carga:
    #Las constantes estan en unidades de e y nm
    e = 1
    k = 2.306934E-10
    #Iniciar las variables
    def __init__(self, x0, y0, signo0):
        self.x=x0
        self.y=y0
        self.signo=signo0
        
    def distancia(self, X, Y):
        d = np.sqrt((X-self.x)**2 + (Y-self.y)**2)
        return d
    def signo(self):
        return signo
    def potencial(self, distancia):
        epsilon = 0.01
        potencial = (Carga.k*Carga.e)/(distancia+epsilon)
        if(self.signo == True):
            return potencial
        else:
            return -potencial

#Inicializando las cargas 
q1 = Carga(0.5,0.5,False)
q2 = Carga(0.5,-0.5,True)
q3 = Carga(-0.5,0.5,True)
q4 = Carga(-0.5,-0.5,False)
cargas =[q1,q2,q3,q4]

#POTENCIAL
N = 200
x = np.linspace(-1,1,N)
y = np.linspace(-1,1,N)

def sum_v(X,Y):
    V_t = 0
    for q in cargas:
        V_t += q.potencial(q.distancia(X,Y))
    return V_t
X,Y = np.meshgrid(x,y)
Z = sum_v(X,Y)

#CAMPO
def derivada_cx(xs,ys,h):
    derivada_c = (sum_v(xs+h/2,ys)-sum_v(xs-h/2,ys))/h
    return derivada_c
def derivada_cy(xs,ys,h):
    derivada_c = (sum_v(xs,ys+h/2)-sum_v(xs,ys-h/2))/h
    return derivada_c

h_y  = abs(y[0]-y[1])
h_x = abs(x[0]-x[1])
E_y = derivada_cy(X,Y,h_y)
E_x = derivada_cx(X,Y,h_x)

#GRAFICA
fig = plt.figure(figsize=(8,6))
plt.streamplot(X, Y, -E_x, -E_y, density=1.2, color='k', linewidth=1)
#plt.imshow(Z,cmap='magma',extent=[-1,1,-1,1], alpha=14)
plt.pcolormesh(X,Y,Z,cmap='magma', alpha=14)
plt.title('Potencial y líneas de campo', fontsize=20)
plt.xlabel(r'$x(nm)$', fontsize=12)
plt.ylabel(r'$y(nm)$', fontsize=12)
bar = plt.colorbar()
bar.set_label(r'Potencial $(N \cdot nm \cdot e^{-1}$)', 
    rotation=270, fontsize= 7.5)
fig.tight_layout()
k_patch = mpatches.Patch(color='k', label=r'Campo $\vec{E}$')
blue_patch = mpatches.Patch(color='blue', label='The blue data')
plt.legend(handles=[k_patch],loc='upper right', 
    frameon=True,framealpha=0.7,facecolor='gold',shadow=True)
plt.savefig('cargas.pdf')