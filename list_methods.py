# 1) append() :- This method adds new items to the original list.

print("Output for append method")
l=[1,3,7,67]
print(l)

# l.append(91,93) ----> append methods takes one and only one argument

l.append(92)
print(l)


# 2) sort() :- This method sorts the items of list in ascending order. The original list is updated.

print("Output for sort() method")
l1=[1,33,21,24,43,77]
l1_1=['blue',"green","violet",'red',"saffron"]
print(l1)
l1.sort()
print(l1)
print(l1_1)
l1_1.sort()
print(l1_1)

# ----> Even i can print list items in descending order.

print("Output for sort() method but in descending")
l1.sort(reverse=True)
print(l1)

# 3) reverse() :- This method reverses the order of the list and  the original list is updated.

print("Output for reverse() method")
l2=[22,23,34,33]
print(l2)
l2.reverse()
print(l2)

# 4) index() :- This method returns the index of the first occurence of the list item.

print("Output for index() method")
l3=[77,32,33,43,345,3442,22,27,22,27]
a=l3.index(27)
b=l3.index(22)
print("The return value given by method index() for",27,"and",22,"is",a,"and",b)

# 5)  count() :- This method returns the count of the number of items with the given value.

print("Output for count() method")
l4=[22,23,32,12,22,37,22,87]
c=l4.count(22)
print("The number of times",22,"is present in l4 is",c)

'''
# 6) copy() :- This method returns copy of the list.This can be done to perform
# operations on the list WITHOUT MODIFYING THE ORIGINAL LIST.
'''

# PROBLEM IF I DON'T USE COPY METHOD :-

print("Problem if i don't use copy() method")
l4=[22,32,34,43,47]
print(l4)
l4_1=l4
print(l4_1)
l4_1[0]=77
print(l4)
print(l4_1)

'''
ANS - Even if i change in the copy list then it is changing the same 
thing in the original list
'''

print("Output after using copy() method")
l5=[22,33,23,43,47,76]
print(l5)
l5_copy=l5.copy()
print(l5_copy)
l5_copy[2]=433
print(l5)
print(l5_copy)

'''
7) insert() :- This method inserts an item at the given index. User 
has to specify index and the item to be inserted within the insert() method
'''

print("Output after using insert() method")
l6=[22,23,76,60,34]
print(l6)
l6.insert(3,56)
l6.insert(4,74)
print(l6)


'''
8) extend() :- This method adds an entire list or any other collection
datatype(set,tuple,dictionary) to the existing list
'''

print("Output after using extend() method")
l7=[29,76,66,67,97]
l7_1=[200,202,322]
print(l7)
l7.extend(l7_1)
print(l7)