try:
    a=int(input("Enter a number : "))
    a1=[6,7,6.6]
    print(a1[a])
except IndexError as e:
    print(e)
    print("Index error")
except ValueError as e1:
    print(e1)
    print('Number entered is not an integer.')