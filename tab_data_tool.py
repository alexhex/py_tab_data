#!usr/bin/python3
#-*-coding:utf-8-*-



import re
import os


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


# *formulate a reference packer attribute list in a dictionary called ref_tab_data

ref_tab_data = {}
condensed_ref_tab_data = {}

filename = "in.txt"
refpath = os.path.join(folderpath, filename)
str_in = open(refpath, 'r')
line = '1'
att = ''
val = ''

while(line):
    line = str_in.readline()
    if line.find('=') == -1:
        break
    [att, val] = line.split('=', 1)
    att = att.strip()
    val = val.strip()
    ref_tab_data[att] = val
    condensed_ref_tab_data[(re.sub(r'\W', '', att))] = val

str_in.close()

# *Choose a pre-defined packer type

packer_types = []
filename = "packertypes.txt"
packer_type_path = os.path.join(folderpath, filename)
str_in = open(packer_type_path, 'r')
line = '1'

while(line):
    line = str_in.readline().strip()
    packer_types.append(line)

print (packer_types)


print (ref_tab_data)
print (condensed_ref_tab_data)

str_in.close()
