#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyPDF2, os

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "October 2nd, 2019"
__final_date__ = "March 25, 2023"

"""
This script can merge all the pdf files in the current directory
Usage: python merge-pdf.py
revision history:
    creation date: October 2nd, 2019
    March 25, 2023. Updated to PyPDF2 version 3.0.0
"""

#output file name
print("The output name will be named 'merged_file.pdf'!")
output_filename = 'merged_file.pdf'

# Get all pdf file names
pdffiles = []
for filename in os.listdir('.'): #return all the files in current dir.
    if filename.endswith('.pdf') and filename!=output_filename:
#         print(filename)
        pdffiles.append(filename)
pdffiles.sort(key=str.lower)   # sort
print('Please check the sequence is that you expect:\n')
for i in pdffiles:
    print(i)

# pdfwriter = PyPDF2.PdfFileWriter()   
pdfwriter = PyPDF2.PdfWriter()   
    
for file in pdffiles: # loop all pdf files
    open_file = open(file, 'rb')
    # read_file = PyPDF2.PdfFileReader(open_file)
    read_file = PyPDF2.PdfReader(open_file)
    
    # loop through all the PDF pages
    # this loop will copy all pages to the object of PdfFileWriter
    # for page_number in range(0,read_file.numPages):
    for page_number in range(0,len(read_file.pages)):
        # page_object = read_file.getPage(page_number)
        page_object = read_file.pages[page_number]
        # pdfwriter.addPage(page_object)
        pdfwriter.add_page(page_object)
        
# save the merged PDF
with open(output_filename, 'wb') as f:
    pdfwriter.write(f)
