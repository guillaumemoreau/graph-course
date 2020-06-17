
GENFIG=genfig/ft0.tex 

slides.pdf: slides.tex definitions.tex introduction.tex parcours.tex pcc.tex $(GENFIG)
	lualatex slides 

# Les exemples "externes" 

exemples: exemples/exemple-pp.pdf exemples/exemple-pl.pdf exemples/exemple-biparti.pdf 

exemples/exemple-pp.pdf: exemples/exemple-pp.tex genfig/pp-0.tex genfig/pp-1.tex genfig/rg-1.pdf genfig/rg-11.pdf
	lualatex exemples/exemple-pp 

genfig/pp-0.tex: snippets/parcours-profondeur.py 
	python3 snippets/parcours-profondeur.py 
	mv pp-*.tex genfig 

genfig/rg-0.tex: snippets/exemple-pp.py 
	python3 snippets/exemple-pp.py 
	mv rg-*.pdf genfig 

exemples/exemple-pl.pdf: exemples/exemple-pl.tex genfig/pl-0.tex genfig/pl-12.tex 
	lualatex exemples/exemple-pl 

genfig/pl-0.tex: snippets/parcours-largeur.py 
	python3 snippets/parcours-largeur.py 
	mv pl-*.tex genfig 

exemples/exemple-biparti.pdf: snippets/biparti.py genfig/biparti-1.pdf genfig/biparti-12.pdf 
	lualatex exemples/exemple-biparti

genfig/biparti-1.pdf: snippets/biparti.py 
	python3 snippets/biparti.py 
	mv biparti-*.pdf genfig 

# Exemples internes (i.e. dans le poly)


genfig/ft0.tex:
	python3 snippets/fermeture-transitive.py 
	mv ft*.tex genfig 

