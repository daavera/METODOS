#Generador de la Tarea 3
Resultados_hw3.pdf : Resultados_hw3.tex grafica_p_1.png grafica_o_1.png grafica_o_2.png
	pdflatex $< 

grafica_p_1.png : datos_p_1.csv

datos_p_1.csv : coordinates.csv Planetas.c Planetas.x Plots_planetas.py
		cc Planetas.c -lm -o Planetas.x
		./Planetas.x > datos_p_1.csv
		python Plots_planetas.py
	
grafica_o_1.png : Onda.py
	python $^
	touch grafica_o_2.png


grafica_o_2.png : Onda.py
	python $^
	touch grafica_o_1.png