# VARIABLE LENGTH ARGUMENTS

'''
1) Arbitrary arguments :-
While creating a function, pass a * before the parameter name while
defining the function.The function accesses the arguments by processsing
them in the form of tuple.
'''

def name(*name):
    print("The type of parameter is",type(name))
    print("Hello",name[0],name[1],name[2])
name('Haria','Rakshit',"Raka","Binod")