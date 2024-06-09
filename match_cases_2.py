x=int(input('Enter the number : '))
match x:
    case 0:
        print("X is 0")
    case 7:
        print("X is 7")
    case _ if(x>0 and x<100):
        print('x i between 0 and 100')
    case _ if x>=100 and x<=200:
        print("X is between 100 and 200")