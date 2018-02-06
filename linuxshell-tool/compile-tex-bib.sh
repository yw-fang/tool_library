#author: Y.-W. FANG
#contact: fyuewen@gmai.com
#purpose: in case you get an latex error like
#"I couldn't open file name 'myBib.aux'"
#you can use this script to compile the tex so that the references can
#be displayed sucssfully. Please ensure pdflatex is installed.
pdflatex LiOsO3-DFT-manu.tex 
bibtex *.aux
pdflatex LiOsO3-DFT-manu.tex 
pdflatex LiOsO3-DFT-manu.tex 

#references:
#https://tex.stackexchange.com/questions/64696/bibtex-i-couldnt-open-file-name-mybib-aux
