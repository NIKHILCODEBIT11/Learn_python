x=int(input('Enter the number :'))
match x:
    case 0:
        print('X is 0')
    case 2:
        print("X is 2")
    case _:
        print("Default value is",x)