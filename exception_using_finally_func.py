def func1():
    try:
        l1=[3,5,4,55,65,'hi',7.7]
        i=int(input('Enter the value of index : '))
        print(l1[i])
        return 1
    except:
        print('Some error occured')
        return 0
    finally:
        print("I am always executed")
func1()