# # f=open('myfile.txt','a')
# # f.write('Hi ')

# with open('myfile.txt','r') as f:
#     t=f.read()
#     print(t)

f=open('myfile.txt','r')
i=0
while True:
    i+=1
    tx=f.readline()
    print(tx)
    if not tx:
        break
    m1=float(tx.split(",")[0])
    m2=float(tx.split(",")[1])
    m3=float(tx.split(",")[2])
    print(f"Marks scored by {i} is {(m1/80)*100}")
    print(f"Marks scored by {i} is {(m2/80)*100}")
    print(f"Marks scored by {i} is {(m3/80)*100}")


# f1=open('myfile.txt')
# txt=f1.read()
# print(txt)

with open ('myfile_1.txt','w') as f:
    line=['line1','line2','line3']
    for l in line:
        f.writelines(l+'\n')
    f.close()
with open('myfile_1.txt') as f1:
    f2=f1.readlines()
    print(f2)
    print(type(f2))