# EXAMPLE 1

a=input() # SIMPLY WILL TYPE WHAT I WANT AND STORE AS STRING IN a
print(a)  # SIMPLY WILL DISPLAY WHAT I HAVE WRITTEN


# EXAMPLE 2

b=input("Enter the name :") # SIMPLE WILL DISPLAY THE STRING AND WILL TAKE INPUT AND WILL STORE IN b
print("The name is",b)      # SIMPLY WILL DISPLAY THE INPUT STRING ALONG WITH THE STRING USED IN print()


# EXAMPLE 3

c=input("Enter first number : ")
d=input("Enter second number : ")
print("The addition of",c,"and",d,"is",c+d)
'''
For giving input as 3 and 7 i am getting sum as 37 but why ????

REASON - Since whatever i give input by default it is considered as string
untill and unless i typecast it that's why when i give input as 3 and 7 then 
it is stored in variable as string not as integer that's why while adding
i am getting concatenation.
'''

# EXAMPLE 4

e=input("Enter 1st number : ")
f=input("Enter 2nd number : ")
print("The addition of e=",e,"and f=",f,"is",int(e)+int(f))

"""
Since this time i am able to typecast string to integer before the operation
that's why i am getting result as integer.
"""

# EXAMPLE 5

g=int(input("Enter first number:")) # ---> Directly typecasted from str to int
h=int(input("Enter second number:")) # -----> Directly typecasted from str to int
print("The addition of g =",g,"and h =",h,"is",g+h)