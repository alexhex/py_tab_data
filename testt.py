import re
#
# # str_in = open('in.txt', 'r')
#
# line = '1'
#
# while(line):
#     print line
#     line = str_in.readline()
#     print line

print ('this is a test')

matchobj = re.match(r'\=', "a =br")
if matchobj:
    print ("YES")
else:
    print ("No")