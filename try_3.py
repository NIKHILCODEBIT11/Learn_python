with open("file_3.txt",'w') as f:
    f.close()
f=open('file_3.txt','w')
str=input("Enter message : ")
f.writelines(str)
f.close()
with open('file_3.txt','r') as f:
    f1=f.read()
    str=f1
print(f1)
dict={}
count=0
dict.update({'the':0})
list=str.split(" ")
for l in list:
    if l=="the":
        count+=1
dict.update({'the':count})
print(dict)

