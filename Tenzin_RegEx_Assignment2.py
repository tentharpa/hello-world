#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:30:35 2020

@author: tharpa
"""

#import os
import PyPDF2
import re
import pandas as pd
from pathlib import *

dir_path = Path('/Users/tharpa/Desktop/syllabi')      #directory to pdf files
pdf_files = list(dir_path.glob('*.pdf'))              # coverting result to a list

#empty lsit to capture the matched feature
termlist = []
placelist = []
unilist = []
namelist = []
emaillist = []

for i in pdf_files:
    pdfFileObj = open(i, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    pdfdata = pageObj.extractText()
    print(pdfdata)
    
    term = re.compile("[A_Z][a-z]+\s[0-9][0-9][0-9][0-9]")
    place = re.compile("^University\sof ([A-Z][a-z]+\(\s|$\))")
    university = re.compile("^University\s[a-z][a-z]\s[A-Z][a-z]+")
    name_edu = re.compile("[a-z]+\.[a-z][a-z][a-z]")
    email = re.compile("\s+@\s")
    
    if term.search(pdfdata):
        termlist.append(term.search(pdfdata).group())
    else:
        termlist.append('null')
    
    if place.search(pdfdata):
        placelist.append(place.search(pdfdata).group())
    else:
        placelist.append('null')
    
    if university.search(pdfdata):
        unilist.append(university.search(pdfdata).group())
    else:
        unilist.append('null')
        
    if name_edu.search(pdfdata):
        namelist.append(name_edu.search(pdfdata).group())
    else:
        namelist.append('null')
    
    if email.search(pdfdata):
        emaillist.append(email.search(pdfdata).group())
    else:
        emaillist.append('null')
        
    print('-------------------------------------------')
    
df = pd.DataFrame(list(zip(termlist,placelist,unilist,namelist,emaillist)), columns=['Term','Place','university','name','email'])
print(df)