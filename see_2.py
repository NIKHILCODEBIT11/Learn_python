f=open('see_2.txt','r')
i=0
while True:
    line=f.readline()
    if not line:
        break
    i+=1
    m1=line.split(',')[0]
    m2=line.split(',')[1]
    m3=line.split(',')[2]
    print(f'Mark of student {i} in maths is {m1}')
    print(f'Mark of student {i} in phy is {m2}')
    print(f'Mark of student {i} in chem is {m3}')
