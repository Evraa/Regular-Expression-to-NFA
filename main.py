import re

txt = "A|B |C*"
txt = txt.replace(" ","")

res = re.finditer("[|*]", txt)
for r in res:
    print (r.start())

'''
    1- take input
    2- validate
    3- parse
    4- state
    5- jsonify
    6- graph
'''