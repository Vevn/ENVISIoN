SHELL=/bin/bash
FIGS := $(shell find ../technical_documentation/figures -not -path '*/\.*')
LIPS := $(shell find Lips -name '*.tex' -not -path '*/\.*')

all: lips_technical_documentation.pdf

lips_technical_documentation.pdf: lips_technical_documentation.tex technical_documentation_main.tex $(FIGS) $(LIPS)
	NAME=$$(basename "$<" .tex); \
	latexmk -pdf "$$NAME".tex

technical_documentation_main.tex: ../technical_documentation/technical_documentation.rst 
	@echo "Running rst2latex"
	@NAME=$$(basename "$@" .tex); \
	rst2latex --no-section-numbering --use-latex-toc --use-latex-citations "$<" | \
		sed 's/\\hyperref\[\([^]]\+\)\]{[^}]\+}/\\ref{\1}/g' | \
		sed 's/\\phantomsection//g' | \
		perl -pe 'BEGIN{undef $$/;} s/\\section\{[^a-zA-Z]*Referenser[^}]*\\label\{referenser\}[^}]*\}//smg' | \
		perl -pe 'BEGIN{undef $$/;} s/(\\label\{[^}]*\})\s*\\caption\{(.*?)\}\s*\\end\{figure\}/\n\\caption{\2\1}\n\\end{figure}/smg' | \
                awk '/\\section{Bakgrund/{flag=1} /\\end{document}/{flag=0}flag' | \
                cat <(echo -e '% ******************************************************************************************************************\n' \
                              '% ****** !!!WARNING!!! DO NOT EDIT THIS FILE, IT IS AUTOMATICALLY GENERATED FROM technical_documentation.rst  ******\n' \
                              '% ******************************************************************************************************************\n\n') - > "$$NAME".tex; 

clean:
	rm -f *~
	latexmk -c lips_technical_documentation.tex
	rm -f technical_documentation_main.tex
