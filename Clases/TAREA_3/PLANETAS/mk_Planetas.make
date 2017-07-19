python_planetas.py : datos_planetas.csv
	./planetas.x > datos_planetas.csv
planetas.x : planetas.c
	cc planetas.c -lm -o planetas.x

	