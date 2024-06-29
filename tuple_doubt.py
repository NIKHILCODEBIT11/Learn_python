tuple_1=(1,2,3,"hello",("hii",3,"money"),9*7,"run",True)
if 'hello' in tuple_1:
    print("Yes, 'hello' is present")
else:
    print("No, it is not present")

for i in tuple_1:
    k=str(i)
    print(k)
    if len(k)>1:
        for j in k:
            print(j)
            if j=="money":
                print('yes,money is present')
            else:
                print('No, money is not present')