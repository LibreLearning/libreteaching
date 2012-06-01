# $Id: Makefile 4229 2006-06-21 22:20:33Z jjamor $

all: slides.pdf

slides.pdf: slides.tex

	(cd figs ; sh generapdf)

	pdflatex slides

clean:
	rm -f slides.dvi slides.ps *.snm *.out *.nav *.log *.aux *.toc *.vrb *.pdf *~
	(cd figs; rm -f *.pdf)
