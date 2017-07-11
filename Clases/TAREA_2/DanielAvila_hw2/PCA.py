## TAREA 2 - PCA
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

datos = pd.read_csv('DatosBancoMundial5.csv', ',')

#Organizacion de los datos
datos = datos.set_index('Series Name').T.iloc[3:,:]
index = list(datos.columns.values)
datos = (datos-datos.mean(axis=0))/datos.std(axis=0)
num_r , num_c = np.shape(datos)

#Generación de colores aleatorios extraida de Stack-Overflow
from random import randint
colors = []
for i in range(num_c):
    colors.append('#%06X' % randint(0, 0xFFFFFF))

#Grafica de los datos normalizados
f1 , ax = plt.subplots(5,1, figsize=(10,8), sharex=True)

###Generación de colores aleatorios extraida de Stack-Overflow
from random import randint
colors = []
for i in range(num_c):
    colors.append('#%06X' % randint(0, 0xFFFFFF))

###Etiquetas de paises
paises = datos.T.columns.tolist()
labels = []
for i in range(np.size(paises)):
    labels.append(paises[i].split('[')[1].split(']')[0])
    
###Grafica 
x = np.arange(num_r)
for i in range(num_c):
    label = index[i]
    d = datos.iloc[:,i].values
    ax[i].plot(d, color = colors[i])
    ax[i].set_title(index[i])
plt.tight_layout()
plt.xticks(x[::5],labels[::5],rotation='vertical')
plt.savefig('ExploracionDatos.pdf', bbox_inches='tight')


#Matriz de covarianza
def matriz_cov(num_c,num_r,datos):
    combinaciones = np.array(np.meshgrid(range(num_c),range(num_c))).T.reshape(-1,2)
    matriz_cov = np.empty([num_c,num_c])
    for i , j in combinaciones:
        dt = datos
        dat_i = dt.iloc[:,i].values
        dat_j = dt.iloc[:,j].values
        n_var = (dat_i) * (dat_j)
        sum_var = np.sum(n_var)
        matriz_cov[i,j] = sum_var/(num_r-1)
    return matriz_cov

#Calculo de la matriz de covarianza y de los eigenvec/val
cov = matriz_cov(num_c,num_r,datos)
values , vectors = np.linalg.eig(cov)
percent = []
for val in values:
    percent.append((val*100)/np.sum(values))
print('El componente principal es: %s , el segundo componente principal es: %s \n' % (vectors[:,0],vectors[:,1]))

#Grafica de datos en los nuevos ejes
PCA_1 = []
PCA_2 = []

for i in range(num_r):
    PCA_1.append(np.dot(datos.iloc[i,:].values,vectors[:,0]))
    PCA_2.append(np.dot(datos.iloc[i,:].values,vectors[:,1]))

f2 = plt.figure(figsize=(10,6))
plt.scatter(PCA_1,PCA_2, color='turquoise', s = 40, alpha = 0.5)
plt.title('Datos en los ejes PCA 1 y PCA 2', fontsize=16)
plt.xlabel('PCA 1', fontsize=12)
plt.ylabel('PCA 2', fontsize=12)
plt.grid(True, alpha=0.2)
plt.savefig('PCAdatos.pdf')

#Grafica de variables agrupadas
f3 = plt.figure(figsize=(10,6))
for i in range(num_c):
    plt.scatter(vectors[i,0],vectors[i,1], s = 300 ,label=index[i], alpha = 0.5, color = colors[i])
lgd = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.09),
          fancybox=True)
plt.axhline(y=0, color='k', linewidth=1.0)
plt.axvline(x=0, color='k', linewidth=1.0)
plt.title('Variables en los ejes PCA 1 y PCA 2', fontsize=16)
plt.xlabel('PCA 1', fontsize=10)
plt.ylabel('PCA 2', fontsize=10)
plt.grid(True, alpha=0.2)
plt.savefig('PCAvariables.pdf',bbox_extra_artists=(lgd,), bbox_inches='tight')
print('Las variables que estan correlacionadas son %s & %s \n' 
	%([index[0],index[1]],[index[2],index[3]]))
