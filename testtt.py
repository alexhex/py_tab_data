#!/usr/bin/python3
#-*-coding:utf-8-*-

import csv, sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (col1, col2);")