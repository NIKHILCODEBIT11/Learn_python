num=int(input("Enter a number :"))
if(num<0):
    print("Number is negative") # This is the level of indent for 1st if-else block
elif(num>0):
    if(num>0 and num<=10):  
        print("Number is between 1 and 10") # This is the level of indent for this nested if-else block
    elif(num>10 and num<=20):
        print("Number is between 10 and 20") # This is the level of indent for this nested if-else block
    else:
        print("Number is greater than 20") # This is the level of indent for this nested if-else block
else:
    print("Number is zero")   # This is the level of indent for 1st if-else block 