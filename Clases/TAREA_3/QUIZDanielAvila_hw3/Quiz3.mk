all : posBalon.pdf velBalon.pdf

posBalon.pdf : Balon.py
	python $^

velBalon.pdf : Balon.py
	python $^
