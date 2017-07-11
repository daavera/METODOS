import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
plt.style.use('ggplot')

datos = np.loadtxt('datos_CAMINATA.txt')

#Distribucion binomial
fig = plt.figure(figsize=(7,4))
plt.hist(datos[0],normed=True, bins=10, alpha = 0.8, label='Datos')
plt.legend()
plt.title('Distribución Binomial')
plt.savefig('binomial.png')

#Distribucion normal
##Generar la lista
suma = []
for row in datos:
    suma.append(np.sum(row))
suma = np.array(suma)
##Graficar el histograma
fig = plt.figure(figsize=(7,4))
plt.hist(suma,normed=True, bins=20, alpha = 0.8, label = "Datos")
hist, bins = np.histogram(suma, bins=20, normed = True)
x=np.linspace(np.min(bins),np.max(bins),1000)
##Función de ajuste al histograma
mu, sig = norm.fit(suma)
p = norm.pdf(x, mu, sig)
plt.plot(x,p, linewidth=2, label='Ajuste')
plt.legend()
plt.title('Distribución Normal')
plt.savefig('normal.png')

#Media de la binomial
mu_bin = mu/1000
print("La media de la distribución binomial, por Teorema del Límite Central, es %f" %(mu_bin))

#Probabilidad de sacar cara
prob = mu_bin/10
print('La probabilidad de sacar una cara con esta moneda es : %f' %(prob))
