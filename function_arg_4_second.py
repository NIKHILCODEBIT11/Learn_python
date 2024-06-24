'''
VARIABLE LENGTH ARGUMENTS :-

ARBITRARY ARGUMENTS 
'''

def average(*numbers):
    print("The type of parameter is",type(numbers))
    sum=0
    print(numbers)
    for i in numbers:
        sum=sum+i
    print("The average is",sum/len(numbers))
average(7,77,66,55,56,76,87)