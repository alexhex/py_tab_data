#!/usr/bin/python3
#-*-coding:utf-8-*-


import xlwings as xw
import sqlite3
from bottle import route, run, debug, template, request, static_file, error

#指定文件路径，并打定文件
xlsx_path = r"/Users/alexhex/Scripts/BluePack_ESP_examples.xlsx"
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
main_key = 'part_number'
main_format_type = 'INTEGER' 

c.execute('CREATE TABlE {tn} ({nf} {ft} PRIMARY KEY)' \
          .format(tn=table_name, nf=main_key, ft=main_format_type))

# conn.commit()
# conn.close()


# 增加各项列
first_row = raw_table.pop(0)
for item in first_row:
    print (item)
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
               .format(tn=table_name, cn=item, ct=main_format_type))

# conn.commit()
# conn.close()


# 插入后续各行
for item in raw_table:
    try:
        c.execute("INSERT INTO {tn}, ({idf}, {cn}) VALUES (item)\
            .format(tn=table_name, cn=item, ct=main_format_type)