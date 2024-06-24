'''
VARIABLE LENGTH ARGUMENTS :-

Keyword arbitrary arguments :-
While creating a function, pass a ** before the parameter name while
defining the function. The function accesses the arguments by processing
them in the form of dictionary.
'''

def name(**name):
    print("The type of parameter is",type(name))
    print("Hello",name["fname"],name['mname'],name["lname"])
name(mname='sahara',fname='Binod',lname='sahay')
print("The type of paramter as seen from outside of function is",type(name))
