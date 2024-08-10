# am
i='am running'
print(i)
i=i.split(' ')
print(i)
i1=list(i[0])
i2=list(i[1])
print(i1)
print(i2)
a1=i1[1]
i1[1]=i1[0]
i1[0]=a1
print(i1)