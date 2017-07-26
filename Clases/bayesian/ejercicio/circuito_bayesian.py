import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("CircuitoRC.txt")
t = datos[:,0]
carga = datos[:,1]

def likelihood(y_obs,y_model):
	chi2 = 0.5*np.sum((y_obs-y_model)**2)*0.0001
	return np.exp(-chi2)


def model(t_obs,R,C):
	Q_max = 10 * C
	return Q_max*(1-np.exp(-t_obs/(R*C)))

#Primer intento
R_walk = np.empty((0))
c_walk = np.empty((0))
l_walk = np.empty((0))

R_walk = np.append(R_walk, np.random.random())
c_walk = np.append(c_walk, np.random.random())

carga_mod = model(t,R_walk[0],c_walk[0])
l_walk = np.append(l_walk, likelihood(carga,carga_mod))

# Num. de iteraciones
n_iterations = 20000

#Comparación del modelo_new con el _old
for i in range(n_iterations):
	sigma = 0.1
	R_prime = np.random.normal(R_walk[i],sigma)
	c_prime = np.random.normal(c_walk[i],sigma)

	carga_mod = model(t,R_walk[i],c_walk[i])
	carga_prime = model(t,R_prime,c_prime)

	l_prime = likelihood(carga, carga_prime)
	l_init = likelihood(carga, carga_mod)

	alpha = l_prime/l_init
	if(alpha>=1.0):
		R_walk  = np.append(R_walk,R_prime)
		c_walk  = np.append(c_walk,c_prime)
		l_walk = np.append(l_walk, l_prime)
	else:
		beta = np.random.random()
		if(beta<=alpha):
			R_walk = np.append(R_walk,R_prime)
			c_walk = np.append(c_walk,c_prime)
			l_walk = np.append(l_walk, l_prime)
		else:
			R_walk = np.append(R_walk,R_walk[i])
			c_walk = np.append(c_walk,c_walk[i])
			l_walk = np.append(l_walk, l_init)

max_likelihood_id = np.argmax(l_walk)
best_R = R_walk[max_likelihood_id]
best_c = c_walk[max_likelihood_id]

f1 , ax = plt.subplots(1,2, sharey=True,figsize=(10,6))
ax[0].scatter(R_walk, -np.log(l_walk),edgecolor= 'k')
ax[0].set_ylabel("Likelihood")
ax[0].set_xlabel("R")
ax[1].scatter(c_walk, -np.log(l_walk),edgecolor= 'k')
ax[1].set_xlabel("C")
plt.suptitle("Parámetros generados por el método bayesiano")
plt.savefig("R-C_likelihood.png")



f2 , ax = plt.subplots(1,2,figsize=(10,6))
ax[0].hist(R_walk, 20, normed=True,edgecolor='black')
ax[0].set_xlabel("R")
ax[1].hist(c_walk, 20, normed=True,edgecolor='black')
ax[1].set_xlabel("C")
plt.suptitle("Histrogramas de R y C")
plt.savefig("R-C_hist.png")



best_carga = model(t,best_R,best_c)
fig = plt.figure(figsize=(10,6))
plt.scatter(t,carga, edgecolor= 'k', color= 'darkslateblue', s=30 , alpha=0.5, label="Datos")
plt.plot(t,best_carga, color='red', label="Ajuste Bayesiano", linestyle="--", linewidth=3)
plt.legend()
plt.grid(True,alpha=0.3)
plt.xlabel(r"$Tiempo \, (s)$")
plt.ylabel(r"$Carga \, (C)$")
plt.title("Estimación Bayesiana de parámetros")
print("R = %f \nC = %f \nQmax$ = %f$" %(best_R,best_c,best_c*10))
plt.savefig("circuito_bayesian.png")
