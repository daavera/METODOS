PuntoNemo.pdf : Plots.py
	python $^

Plots.py : results.txt

results.txt : GeographicPoint.x
		./$^

GeographicPoint.x : GeographicPoint.c
	cc $^ -lm -o $@

