#-*conding:utf-8-*-


import re
import os


# *get one standard attribute list and a condensed standard attribute list in which
# *all the attributes contains no special characters


std_attr_lst = []
condensed_std_attr_lst = []
line = '1'
lst_path = r'/Users/alexhex/Scripts/Py_Tab_Data/Attributes_List.txt'
lst_in = open(lst_path, 'r')
while(line):
    line = lst_in.readline()
    line = line.strip()
    std_attr_lst.append(line)
    line = re.sub('\W', '', line)
    condensed_std_attr_lst.append(line)
lst_in.close()


# *formulate a reference packer attribute list in a dictionary called ref_tab_data

ref_tab_data = {}
path = r'/Users/alexhex/Scripts/Py_Tab_Data/in.txt'
str_in = open(path, 'r')
line = '1'
att = ''
val = ''

while(line):
    line = str_in.readline()
    [att, val] = line.split('=', 1)
    att = att.strip()
    val = val.strip()


    print "att"
    print "val"

str_in.close()
