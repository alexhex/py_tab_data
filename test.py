#!/usr/bin/python3
#-*-coding:utf-8-*-
# updated by XNiu2 on 11-Feb-2018

import xlwings as xw
import sqlite3
from bottle import route, run, debug, template, request, static_file, error
import os

#指定文件路径，并打开文件
folderpath = os.path.dirname(os.path.abspath(__file__)) 
spreadsheetname = "BluePack_ESP_examples.xlsx"
xlsx_path = os.path.join(folderpath, spreadsheetname) 
# xlsx_path = r"/Users/alexhex/Scripts/BluePack_ESP_examples.xlsx"
# xlsx_path = r"C:\XNiu2\scripts\py_tab_data\tab_data_tool\BluePack_ESP_examples.xlsx"
wb = xw.Book(xlsx_path)


#打开sheets的三种方式

#打开第一个 sheet
sht = wb.sheets[0]
#打开名字为 "aaabbb" 的 sheet
# sht = wb.sheets["aaabbb"]
# 打开当前活动的 sheet
# sht = wb.sheets.active


# 读写数据
raw_table = sht.range("A1:BI13").value
# print (raw_table)


# 创建数据表
conn = sqlite3.connect('tab_data.sqlite')
c = conn.cursor()


table_name = 'bluepack_esp_tab_data'
main_key = 'Name'
main_format_type = 'TEXT' 

c.execute('CREATE TABlE {tn} ({nf} {ft} PRIMARY KEY)' \
          .format(tn=table_name, nf=main_key, ft=main_format_type))

# conn.commit()
# conn.close()


# 增加各项列
first_row = raw_table.pop(0)
attributes = first_row[1:]

for item in attributes:
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=item, ct=main_format_type))

# conn.commit()
# conn.close()


# 插入后续各行

#Test 
# c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES ('102046433', '102046433')" .\
#     format(tn=table_name, idf=main_key, cn='Name'))
# c.execute("UPDATE {tn} SET {cn} = 'AD' WHERE {idf} = '102046433' ".\
#     format(tn=table_name, idf=main_key, cn='Rev'))


#Insert the data:
# i = 0
for item in raw_table:
    part_number = str(int(item[0]))
    raw_command1 = "INSERT INTO 'bluepack_esp_tab_data' ('Name', "
    (raw_command2, raw_command3) = ("", ") VALUES ('%s', " % part_number)
    for a, b in zip(attributes, item[1:]):
        # if type(b) is float:
            # b = str(int(b))
        # print (table_name, main_key, a, part_number, b)
        raw_command2 += "'%s', " % a
        raw_command3 += "'%s', " % b
    #     i += 1
    #     if i > 5:
    #         break
    # i = 0
    # print ((raw_command1+raw_command2[:-2]+raw_command3)[:-2] + ")")
    c.execute((raw_command1+raw_command2[:-2]+raw_command3)[:-2] + ")")
        # try:
        #     print ('insert')
        #     c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES ({pn}, {val}) " .\
        #         format(tn=table_name, idf=main_key, cn=a, pn=part_number, val=b ))
        # except sqlite3.OperationalError:
        #     print ('update')
        #     c.execute("UPDATE {tn} SET {cn} = {val} WHERE {idf} = {pn} " .\
        #         format(tn=table_name, cn=a, val=b, idf=main_key, pn=part_number))

conn.commit()
conn.close()
