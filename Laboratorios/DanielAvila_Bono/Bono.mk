grafica_conveccion.png : plots.py
	python plots.py

plots.py : data.csv
	./conveccion.x > data.csv

data.csv : conveccion.x 

conveccion.x : conveccion.c 
	cc conveccion.c -lm -o conveccion.x