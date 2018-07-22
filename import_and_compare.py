#!usr/bin/python3
#-*-coding:utf-8-*-

# Alexhex 2018-07-07

import os
import re


# *get one standard attribute list and a condensed standard attribute list in which
# *all the attributes contains no special characters


folderpath = os.path.dirname(os.path.abspath(__file__))
filename = "Attributes_List.txt"

std_attr_lst = []
condensed_std_attr_lst = []
line = '1'
lst_path = os.path.join(folderpath, filename) 
lst_in = open(lst_path, 'r')
while(line):
    line = lst_in.readline()
    line = line.strip()
    std_attr_lst.append(line)
    line = re.sub(r'\W', '', line)
    condensed_std_attr_lst.append(line)
lst_in.close()


# Get the attributes list in the file of filename

filename = "MRP.txt"
packer_type_path = os.path.join(folderpath, filename)
line = '1'
count = 1
packer_file = open(packer_type_path, 'r')
while(line):
    line = packer_file.readline().strip()
    if std_attr_lst.count(line) == 0:
        print ("Warning, Attribute %s is not standard!" % line)
        break
    else:
        print ("Line %s is Ok!" % count)
    count += 1
packer_file.close()
        
