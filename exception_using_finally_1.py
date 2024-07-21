try:
    l1=[2,3,4,5,6,7]
    i=int(input('Enter the index value : '))
    print(l1[i])
except:
    print('some error occured.')
finally:
    print('I am always executed.')