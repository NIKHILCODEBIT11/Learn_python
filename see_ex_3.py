i=0
l=[]
l8=[]
i4=0
with open ('see_ex_3.txt','r') as f:
    for i1 in f.readlines():
        i+=1
print('The number of lines are',i)
f.close()
f=open('see_ex_3.txt','r')
i2=0
for i in f.readlines():
    i.strip('\n')
    list1=i.split()
    l.extend(list1)
# print(l)
for q in l:
    q1=q.strip(',')
    k1=q1.strip()
    # print(k1)
    if q.isalpha()==True:
        l8.append(q)
    #print(l)
i2+=len(l)
print('Number of words is',i2)
f.close()
z2=[]
with open ('see_ex_3.txt','r') as f:
    for i in f.readlines():
        z1=i.split()
        print(z1)
        z2.extend(z1)
    print(z1)