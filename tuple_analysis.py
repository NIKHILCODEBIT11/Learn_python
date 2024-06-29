tup=(23,34,"hello",33)
print(type(tup),tup)

tup_1=(1,2)
print(type(tup_1),tup_1)

# Below is showing int instead of tuple why ???

tup_2=(1)
print(type(tup_2),tup_2)
'''
The reason due to which it is showing type int not tuple is that python 
compiler will confuse that i am writing an int enclosed in (), so to 
avoid such confusion it is always advised to give comma '''

tup_2_1=(1,)
print(type(tup_2_1),tup_2_1)