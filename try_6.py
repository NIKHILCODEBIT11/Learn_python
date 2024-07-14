import re
str=input("e")
pattern="[0-9{2}/0-9{2}/0-9{4}]"
s=re.findall(pattern,str)
print(s)