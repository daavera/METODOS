import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

#Funcion en 10-D
def f (X):
    y = 0
    for i in range(10):
        x = X[i]
        y += x
    return y**3

#Generación de x_r & y_r
def random(n_random, X):
    RANDOM =[]
    for z in range(11):
        r = np.random.rand(n_random)
        r = r.tolist()
        RANDOM.append(r)
    RANDOM = np.array(RANDOM)
    for j in range(10):
        RANDOM[j] = RANDOM[j] * np.max(X[j])-np.min(X[j]) + np.min(X[j])
    random_y = RANDOM[10] * np.max(y)-np.min(y) + np.min(y)
    return random_y, RANDOM
#Integral motecarlo
def integral_m(x,y,a,b,n_random):
    y_rand , x_rand = random(n_random, x)
    #Ptos adentro
    delta = f(x_rand) - y_rand
    inside = np.where(delta>0.0)
    #Intervalo
    interval_I = ((b - a) ** 10.0) * (np.max(y)-np.min(y))
    #Integral
    I  = interval_I * (np.size(inside)/(1.0*np.size(y_rand)))
    return I

#Definición de los limites
a = 0
b = 2
N = 1000
n_random = 10000
#Definicion de la función 
X = []
for i in range(10):
    x = np.linspace(a,b,N)
    X.append(x)
y = f(X)

######MONTE CARLO

##Integral promedio (20)
integral = []
for i in range(20):
    #Integración con Monte Carlo
    #Integración con Monte Carlo
    I  = integral_m(X,y,a,b,n_random)
    integral.append(I)
integral = np.array(integral)
prom_integral = np.sum(integral)/len(integral)
print("El promedio de 20 integrales, usando N = 10000, es: %f" %(prom_integral))

##Variación de puntos
n_random_list = np.arange(2,8193,50)
n_integral = []
for n in n_random_list:
    integral = []
    for i in range(20):
    #Integración con Monte Carlo
    #Integración con Monte Carlo
        I  = integral_m(X,y,a,b,n)
        integral.append(I)
    integral = np.array(integral)
    prom_integral = np.sum(integral)/len(integral)
    n_integral.append(prom_integral)
n_integral = np.array(n_integral)

#Grafica
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.ticklabel_format(style='sci',scilimits=(0,6),axis='both')
ax.plot(n_random_list,np.full((1,len(n_random_list)),1126400)[0], linestyle='--', linewidth = 2, label='Integral Analítica', c='g')
ax.plot(n_random_list,n_integral, linewidth = 1, label='Integral numérica', color ='tomato')
plt.grid(True)
plt.ylabel('Valor integral')
plt.xlabel('N')
plt.title('Integral promedio VS. Cantidad de números aleatorios')
ax.fill_between(n_random_list, np.full((1,len(n_random_list)),1126400)[0], n_integral, facecolor='tomato', alpha=0.1)
ax.legend(loc='best', fancybox=True, framealpha=0.5)
plt.savefig('num_integral.pdf')


###Error
int_analitica = 1126400
error = (abs(n_integral-int_analitica)/int_analitica) * 100
sq_N = n_random_list**-(1/2)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(sq_N,error, linewidth = 0.67) 
ax.set_xscale('log')
plt.grid(True)
plt.ylabel('Error relativo porcentual', fontsize=15)
plt.xlabel(r'$\frac{1}{\sqrt{N}}$',fontsize=15)
plt.title(r'Error VS. $\frac{1}{\sqrt{N}}$',fontsize=20)
plt.tight_layout()
plt.savefig('err_integral.pdf')


