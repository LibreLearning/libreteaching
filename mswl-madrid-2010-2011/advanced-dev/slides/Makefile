EMACS=emacs
NAME=python_slides02
EMACS_OPTS=--batch -l ~/.emacs $(NAME).org -f org-export-as-latex

all: pdf

pdf:
	@echo "Generating LaTeX..."
	@$(EMACS) $(EMACS_OPTS)
	@echo "LaTeX generation done"
	@pdflatex $(NAME).tex
	@pdflatex $(NAME).tex
