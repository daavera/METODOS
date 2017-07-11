import numpy as np
import matplotlib.pyplot as plt


lower_limit = 0.0
upper_limit = 1.0

# funcion a integrar
def function(x):
    return np.exp(-x)

# Solucion analítica
def exact(x):
    return -np.exp(-x)
    
# Calculamos el error absoluto entre el valor real de la integral y el calculado por los diferentes métodos.
def error(real, calculated):
    return abs((real-calculated)/real)

    
# Calcular la integral usando MonteCarlo
def montecarlo(f, a, b, n):    
    x = np.random.random(n)
    f_eval = f(x)
    result = f_eval.mean()
    return np.log10(n), result

# Calcular la integral usando metodo de trapezoides
def trapezoid(f, a, b, n):
    x = np.linspace(a, b, n+1)
    h = (b-a)/n
    result = 0
    for i in range(n+1):
        if i == 0 or i == n:
            weight = h/2.
        else:
            weight = h
        result += f(x[i])*weight
    return np.log10(n), result
        
# Calcular la integral usando metodo de simpson
def simpson(f, a, b, n):
    if n%2 == 1:
        n += 1
    h = (b-a)/n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4*f(a + i*h)
    for i in range(2, n-1, 2):
        result += 2*f(a + i*h)
    result *= h/3.
    
    return np.log10(n), result
            
# Calcular la integral usando metodo simpson 3/8
def simpson38(f, a, b, n):
    if n%3 != 0:
        n += 3 - n%3            
    h = (b-a)/n
    result = f(a) + f(b)
    for i in range(1, n, 3):
        result += 3*f(a + i*h)
    for i in range(2, n, 3):
        result += 3*f(a + i*h)
    for i in range(3, n, 3):
        result += 2*f(a + i*h)
    result *= 3*h/8.
    
    return np.log10(n), result
        
# Vamos a calcular la integral
def integrate(func, a, b, n):
    # Llamamos todas la funciones que creamos para calcular la integral. Recordemos que estas funciones retornan dos numeros: el primero es el logaritmo del numero entero usado para integrar y segundo es el valor de la integral calculado.
    montecarlo_results = montecarlo(func, a, b, n)
    trapezoid_results = trapezoid(func, a, b, n)
    simpson_results = simpson(func, a, b, n)
    simpson38_results = simpson38(func, a, b, n)
    
    # creamos una lista con los resultados de las 4 funciones
    results = [montecarlo_results, trapezoid_results, simpson_results, simpson38_results]
    #en la lista "numbers" guardamos los resultados de las integrales por los diferentes metodos
    numbers = [item[0] for item in results]
    #en la lista "errors" guaramos el error de nuestro cálculo con respecto al valor exacto de la integral.
    errors = [np.log10(error(exact_value, item[1])) for item in results]
    
    
    return numbers, errors


#este será el calor exacto de la integral
exact_value = exact(upper_limit) - exact(lower_limit)

#creamos una lista de 20 puntos entre 0 y 10^6
points = 20
numbers = np.logspace(0, 6, points)


#estas listas vacias las usaremos para guardar nuestros valores finales
values_buffer = [[],[],[],[]]
numbers_buffer = [[],[],[],[]]

#estos nombres los usaremos para etiquetar las graficas
names = ["MonteCarlo","Trapezoid", "Simpson", "Simpson 3/8"]

#Ahora inplementaremos la función "integrate" 20 veces recorriendo 6 órdenes de magnitud.
for n in numbers:
    numbers, results = integrate(function, lower_limit, upper_limit, int(n))
    for (values_list, numbers_list, number, result) in zip(values_buffer, numbers_buffer, numbers, results): #Explicar cómo funciona "for" "in zip".
        values_list.append(result)
        numbers_list.append(number)
        
# Graficamos
for (values_list, numbers_list, name) in zip(values_buffer, numbers_buffer, names):
    plt.plot(numbers_list, values_list, "-o", label=name)

plt.legend(loc=3)
plt.xlabel("$\log_{10}n$")
plt.ylabel("$\log_{10}\epsilon$")
plt.grid()
plt.savefig("plots.pdf")
