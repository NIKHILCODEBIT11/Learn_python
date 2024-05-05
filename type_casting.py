# IMPLICIT TYPE CASTING

a3=1.9
b3=2
print("The type of data type a3=1.9 is",type(a3))
print("The type of data type b3=2 is",type(b3))
print("The sum of \"a3\"=1.9 and \"b3\"=2 in implicit typecasting is",a3+b3)
print("The type of data type the sum is",type(a3+b3))

'''
----> HERE SINCE A3 HAS FLOAT VALUE AND HAS HIGHER ORDER SO THE INTEGER 
VALUE OF b3 IS EVEN CONVERTED TO FLOAT VALUE AND ADDITION IS BEEN DONE.
'''


#EXPLICIT TYPE CASTING

# FIRST DEMONSTRATION :-
"""
IF I GIVE ANY VALUE AS STRING TO a AND b AND THEN TRY TO ADD IT THEN IT 
WON'T BE ADDED RATHER IT WILL BE JOINED AS STRING.
"""
a="1"
b="2"
print("The sum of string \"a\"+\"b\" in first demo is",a+b)


# SECOND DEMONSTRATION :-
"""
TYPECASTING STRING WHICH IS VALID INTEGER ENTRY TO INTEGER AND ADDING
 """
a1="1"
b1="7"
print("The sum of string \"a\" and \"b\" in second demo is",int(a1)+int(b1))


# THIRD DEMONSTRATION :-
"""
TRYING TO TYPECAST SUCH A STRING WHICH IS NOT A VALID INTEGER ENTRY
"""
a2="1harish"
b2="4"
print("The sum of string \"a\" and \"b\ in third demo is",int(a2)+int(b2))


