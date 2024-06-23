# TRYING break IN NESTED for LOOP :-

for i in range(4):
    print(4,'*',i,'=',4*i)
    for k in range(7):
        print(7,'*',k,'=',7*k)
        if k==2:
            break