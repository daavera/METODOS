all : Modelo.pdf Param_m.pdf Param_b.pdf

Modelo.pdf Param_m.pdf Param_b.pdf : Param.py
	python $^
