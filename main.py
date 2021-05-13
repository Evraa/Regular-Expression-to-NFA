import re

txt = "A|B |C*"
txt = txt.replace(" ","")

res = re.finditer("[|*]", txt)
for r in res:
    print (r.start())