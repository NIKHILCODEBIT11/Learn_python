def func1():
    try:
        l1=[3,6,7,66]
        i=int(input('Enter the index value : '))
        print(l1[i])
        return 1
    except:
        print('Some error occured')
        return 0
    
    # Without finally :-

    print('I am always executed')
func1()