# 1) Accessing single values :-

# METHOD 1 :-   Mentioning key values in []

info={'Name':"Harish",'Age':19,"Eligible":True}
print(info["Name"])

# METHOD 2 :-   Using get() method

info={'Name':"Harish",'Age':19,"Eligible":True}
print(info.get('Name'))

'''
Diff between both methods :-
Suppose if i try to access the key which is not present in the dict, then 
if use method 1, then it will show error as :-
keyerror
But if i used get() method then it will print :-
None
'''

# Printing non-element key using method 1 :-

# info={'Name':"Harish",'Age':19,"Eligible":True}
# print(info["Etnicity"]) # ---> KeyError: 'Etnicity'


# Printing non-element key using get() :-

info={'Name':"Harish",'Age':19,"Eligible":True}
print(info.get("Etnicity"))


# 2) Accessing multiple values :-

# METHOD 1 :-


# 3) Accessing keys :- I can print all keys in dict using keys() method


info={'Name':"Harish",'Age':19,"Eligible":True}
print(info)
s=info.keys()
k=info.values()
print(info.keys())  # Prints all the keys 
print(info.values()) # Prints all the values
print(type(s))
print(type(k))

# METHOD 2 :-  Using for loop

info={'Name':"Harish",'Age':19,"Eligible":True}
for key in info.keys():
    print(f"The value corresponding to key {key} is {info[key]}")

# 4) Accessing key-value pair :- I can access key-value pair in the dictionary using items() method.

info={'Name':"Harish",'Age':19,"Eligible":True}
a=info.items()
print(info.items())
print(type(a))

for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")