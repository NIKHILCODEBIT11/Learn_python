# Below is an example of using single else statement on a line

a=2
b=337
print('A') if a>b else print("B")

# Below is an example of using multiple else statements on the same line

a=330
b=330
print("A") if a>b else print('=') if a==b else print("B")


'''

Below is the syntax for using short hand if else statements :-


result = value_if_value if condition else value_if_false


********** The above syntax is equivalent to :-

if condition :
   result=value_if_True
else:
   result=value_if_False

'''