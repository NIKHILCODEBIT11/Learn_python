# docstring is written just after the def() below is the example

# 1 :-

def square(n):
    '''
    Takes in a number n, and returns the
    square of n
    '''
    print(n**2)
square(4)
print(square.__doc__)


# 2 :-

# Below is an example where comment is not a docstring

def square_1(m):
    print(m)
    '''
    This is docstring'''
    print(m*m)
square_1(7)
print(square_1.__doc__)

# Since in 2nd code i didn not write comment just after defining function, so it is not docstring.
