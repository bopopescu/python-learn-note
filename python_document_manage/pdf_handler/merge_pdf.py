#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: merge_pdf.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-05 16:08:11
############################

import os
import glob
import PyPDF2

def get_all_pdf_files(path):
    all_pdfs = glob.glob("{0}/*.pdf".format(path))
    all_pdfs.sort(key = str.lower)
    return  all_pdfs

def main():
    all_pdfs = get_all_pdf_files(os.path.expanduser('.'))
    if not all_pdfs:
        raise SystemError('No pdf file found')

    merger = PyPDF2.PdfFileMerger()

    with open(all_pdfs[0], 'rb') as first_obj:
        merger.append(first_obj)

    for pdf in all_pdfs[1:]:
        with open(pdf, 'rb') as obj:
            reader = PyPDF2.PdfFileReader(obj)
            merger.append(filepbj=obj, pages=(1, reader.getNumPages()))

    with open('merge-pdfs.pdf', 'wb') as f:
        merger.write(f)

if __name__ == '__main__':
    main()


