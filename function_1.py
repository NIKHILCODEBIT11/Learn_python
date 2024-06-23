a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
def comp(a1,a2):
    if(a1>a2):
        print("From if block")
        print(a1,"is greater than",a2)
    elif a1==a2:
        print(a1,"is equal to",a2)
    else:
        print("From else block")
        print(a2,"is greater than ",a1)
comp(a,b)