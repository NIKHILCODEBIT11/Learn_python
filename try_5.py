import re
inp=input("Enter string :")
pattern='[0-9]{2}[a-zA-Z]+@[0-9]{2}'
s=re.findall(pattern,inp)
print(s)
