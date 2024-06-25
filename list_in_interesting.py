marks=[3,4,7,"harry",True]
print("Using 'in' keyword to know whether item is present in list or not")

n=int(input("Enter element you want to check : "))
if n in marks:
    print("Yes,",n,"is present in the list")
else:
    print("No,",n,"is not present in the list")
m=str(n)
if m in marks:
    print("yes")
else:
    print("No")