import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("obs_data.dat")
x = datos[:,0]
y = datos[:,1]

#Modelo y likelihood
def model(x,m,b):
    return m*x + b
def likelihood(y_obs,y_mod):
    chi_2 = np.sum((y_obs-y_mod)**2)
    return np.exp(-0.5*chi_2)

#Inicializacion de listas
m = np.empty(0)
b = np.empty(0)
l = np.empty(0)

m_0 = np.random.random()
b_0 = np.random.random()
y_0 = model(x,m_0,b_0)
l_0 = likelihood(y,y_0)

m = np.append(m,m_0)
b = np.append(b,b_0)
l = np.append(l,l_0)

#MC
n_iterations = 10000
for i in range(n_iterations):
    m_prime = np.random.normal(m[i],0.1)
    b_prime = np.random.normal(b[i],0.1)
    y_prime = model(x,m_prime,b_prime)
    l_prime = likelihood(y,y_prime)
    
    alpha = l_prime/l[i]
    if(alpha > 1):
        m = np.append(m,m_prime)
        b = np.append(b,b_prime)
        l = np.append(l,l_prime)
    else:
        beta = np.random.random()
        if(alpha > beta):
            m = np.append(m,m_prime)
            b = np.append(b,b_prime)
            l = np.append(l,l_prime)
        else:
            m = np.append(m,m[i])
            b = np.append(b,b[i])
            l = np.append(l,l[i])

#Mejor ajuste
index = np.argmax(l)
m_mejor = m[index]
b_mejor = b[index]
y_mejor = model(x,m_mejor,b_mejor)
print("Los parámetro encontrados son m= %f y b= %f" % (m_mejor,b_mejor))


#Graficas
f1 = plt.figure(figsize=(10,6))
plt.grid(True,alpha=0.3)
plt.scatter(m,-np.log(l), edgecolor="black")
plt.xlabel(r"$m$")
plt.ylabel(r"$-log(L)$")
plt.title("Convergencia del parámetro m")
plt.savefig("Param_m.pdf")

f2 = plt.figure(figsize=(10,6))
plt.grid(True,alpha=0.3)
plt.scatter(b,-np.log(l), edgecolor="black")
plt.xlabel(r"$b$")
plt.ylabel(r"$-log(L)$")
plt.title("Convergencia del parámetro b")
plt.savefig("Param_b.pdf")

f3 = plt.figure(figsize=(10,6))
plt.grid(True,alpha=0.3)
plt.scatter(x,y, label="Datos")
plt.plot(x,y_mejor, label="Mejor Ajuste")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Mejor ajuste Bayesiano")
plt.savefig("Modelo.pdf")

