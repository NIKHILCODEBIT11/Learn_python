# Factorial :-

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

'''
suppose n=5
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1

'''
n=int(input("enter the number : "))
b=fact(n)
print(f"The factorial of {n} is {b}")