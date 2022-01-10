all:	resume.tex
	platex resume.tex
	pbibtex resume.aux
	platex resume.tex
	platex resume.tex
	dvipdfmx resume.dvi

clean:	resume.pdf
	rm resume.pdf
	rm resume.aux
	rm resume.log
	rm resume.dvi
	
