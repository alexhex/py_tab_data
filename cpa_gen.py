#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [XNiu2 06-Feb-2018]

import xlwings as xw

# input a full filepath to open a workbook
fn = r'C:\XNiu2\New_PKR\2. RFQ\RFQ 246430-7 New QHS\Tab Data_246430-7.xlsx'
wb = xw.Book(fn)

# open the sheet
sht = wb.sheets["QHS"]

# write CPA to the same location and add the table head
file_wr = open(r'C:\XNiu2\New_PKR\2. RFQ\RFQ 246430-7 New QHS\cpa.md', 'w')
file_heada = "|Attribute|Reference Part Number|New Part Number | Class| \r\n"
file_wr.write(file_heada)
file_heada = "|---|----|-----|-----| \r\n"
file_wr.write(file_heada)

# Read and Write data from/to the workbook
# PNRange = sht.range("B2:B1002")
length = range(2, 47)
current_qty = 0

for i in length:
    curr = sht.range('G'+str(i)).value
    if curr != "":
        val = sht.range('A'+str(i)).value
        val2 = sht.range('F'+str(i)).value 
        val3 = sht.range('J'+str(i)).value 
        line = "|%s|%s|%s|  |" % (val, val2, val3)
        file_wr.write(line)
        file_wr.write("\r\n")


file_wr.close()