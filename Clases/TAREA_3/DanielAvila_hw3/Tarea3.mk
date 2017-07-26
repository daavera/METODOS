#Generador de la Tarea 3
Resultados_hw3.pdf : Resultados_hw3.tex grafica_p_1.png grafica_o_1.png grafica_o_2.png
	pdflatex $< 

grafica_p_1.png : datos_p_1.csv

grafica_p_1.png : Plots_planetas.py
		python Plots_planetas.py
	
datos_p_1.csv : Planetas.x
		./Planetas.x > datos_p_1.csv

Planetas.x : Planetas.c
		cc Planetas.c -lm -o Planetas.x

Planetas.c : coordinates.csv
		cc Planetas.c -lm -o Planetas.x

grafica_o_1.png : Onda.py
	python $^
	touch grafica_o_2.png


grafica_o_2.png : Onda.py
	python $^
	touch grafica_o_1.png