#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [XNiu2 16-Jan-2018] 


import xlwings as xw
import string

def min_non_zero(lst):
    mins = lst[0]
    for item in lst:
        if item != 0 and item < mins:
            mins = item
    return mins




# input a full filepath to open a workbook
fn = r"C:\Users\XNiu2\Documents\My Received Files\cost analysis.xlsx"
wb = xw.Book(fn)

# open the sheet
sht = wb.sheets[0]

# Read and Write data from/to the workbook
# PNRange = sht.range("B2:B1002")
length = range(2, 50)
current_qty = 0

for i in length:
    current_qty = sht.range('J'+str(i)).value
    current_list = sht.range('O'+str(i)+':AD'+str(i)).value
    prices = current_list[::2]
    qtys = current_list[1::2]
    current_pair = dict(zip(qtys, prices))
    print (current_pair)
    current_price = min_non_zero(prices)
    for j in qtys:
        if current_qty <= j:
            sht.range('I'+str(i)).value = current_pair[j]
            break
        elif j==0:
            sht.range('I'+str(i)).value = current_price
            break


