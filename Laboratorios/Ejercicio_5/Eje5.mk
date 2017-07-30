results.txt : pi.x
	./$^

pi.x : pi.c
	cc $^ -lm -o $@

pi.c : integracion.x
	./$^

integracion.x : integracion.c
	cc $^ -lm -o $@