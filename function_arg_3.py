'''
REQUIRED ARGUMENTS :-
In case i don't pass the arguments with a key=value pair syntax,then it 
is necessary to pass the arguments in the correct positional order
and the number of arguments passed shoul match with actual definition.
'''
def average(a,b,c=9,d=9):
    print("The average is",(a+b+c+d)/4)
average(b=9,c=9)

'''
IMP CONCEPT :-
I can't pass any required argument after passing even a single default
argument.
'''