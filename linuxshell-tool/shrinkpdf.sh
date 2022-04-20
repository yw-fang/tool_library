echo "useage: shrinkpdf.sh filename"
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dPDFSETTINGS=/ebook -sOutputFile=newFile.pdf $1
