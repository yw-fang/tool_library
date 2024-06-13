echo "useage: shrinkpdf.sh filename"
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dPDFSETTINGS=/ebook -sOutputFile=newFile.pdf $1 
# """
# /screen: Selects low-resolution output similar to the Acrobat Distiller "Screen Optimized" setting (72 dpi).
# /ebook: Selects medium-resolution output similar to the Acrobat Distiller "eBook" setting (150 dpi).
# /printer: Selects output similar to the Acrobat Distiller "Print Optimized" setting (300 dpi).
# /prepress: Selects output similar to the Acrobat Distiller "Prepress Optimized" setting (300 dpi, color preserving).
# """
