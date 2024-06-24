'''
DEFAULT ARGUMENTS :-

I can provide default value while creating a function. This way the 
function assumes a default value even if the value is not passed as 
the argument from calling function.
'''

print("Default arguments are taken as a=2,b=3,c=7")
def avg(a=2,b=3,c=7):
    print("The average of",a,b,c,"is",(a+b+c)/3)
avg()   #----> Default arguments will be passed
avg(77)   #---> a=77 rest values are default arguments
avg(b=9)   #---> b=9 rest values are default arguments
avg(33,44,55)   #---> a=33,b=44,c=55