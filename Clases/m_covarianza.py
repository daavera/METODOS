#MATRIZ DE COVARIANZA

import numpy as np
import pandas as pd

#importar datos
datos = pd.read_csv('room-temperature.csv', sep=',')

datos = datos.ix[:,'FrontLeft':'BackRight']
mean = datos.apply(np.mean)
n_r = np.shape(datos)[0]
n_c = np.shape(datos)[1]
combinaciones = np.array(np.meshgrid(range(n_c),range(n_c))).T.reshape(-1,2)

def matriz_cov(datos):
    matriz_cov = np.empty([n_c,n_c])
    for i , j in combinaciones:
        dat_i = datos.ix[:,i].values
        dat_j = datos.ix[:,j].values
        n_var = (dat_i - mean[i]) * (dat_j - mean[j])
        sum_var = np.sum(n_var)
        matriz_cov[i,j] = sum_var/(n_r-1)
    return matriz_cov
matriz_cov = matriz_cov(datos)
#print(matriz_cov)

values , vectors = np.linalg.eig(matriz_cov)
org_values = []
org_vectors = []
for  i in range(len(values)):
	max_vtemp = 0
	i_max = np.where(values == np.max(values))
	a = int(i_max[0])
	org_values.append(values[a])
	org_vectors.append(vectors[:,a].tolist())
	values[a] = -99999
org_values = np.array(org_values)
org_vectors = np.array(org_vectors).T




