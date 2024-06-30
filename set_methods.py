# 1) union() :-


# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_3=cities_1.union(cities_2)
print("The set after union() in cities_1 is :- \n",cities_3)

# Example 2 :-

s1={1,2,5,6}
s2={3,6,7}
print("The set after union() in s2 is :-\n",s2.union(s1))

'''
In union the original sets are not affected unlike in update() the set 
which is getting updated.
'''

# 2) update() :-


# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_1.update(cities_2)
print("The set after update() in cities_1 is :- \n",cities_1)

# Example 2 :-

s1={1,2,5,6}
s2={3,6,7}
s2.update(s1)
print("The set after update() in s2 is :-\n",s2)

# 3) intersection() :-

# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_4=cities_1.intersection(cities_2)
print("The set after intersection is :-\n",cities_4)

# Example 2 :-

s1={1,2,5,6}
s2={3,6,7}
print("The set after intersection is :-\n",s2.intersection(s1))

# 4) intersection_update() :-

# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_1.intersection_update(cities_2)
print("The set cities_1 after intersection_update() is :-\n",cities_1)

# Example 2 :-

s1={1,2,5,6}
s2={3,6,7}
s2.intersection_update(s1)
print("The set s2 after intersection_update() is :-\n",s2)

# 5) symmetric_difference() :-

# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_3=cities_1.symmetric_difference(cities_2)
print("The set after symmetric_difference() method in cities_1 is :-\n",cities_3)

# Example 2 :-

s1={1,2,5,6}
s2={3,6,7}
print("The set after symmetric_difference() method in s2 is :-\n",s2.symmetric_difference(s1))

# 6) symmetric_difference_update() :-

# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_1.symmetric_difference_update(cities_2)
print("The set after symmetric_difference_update() method in cities_1 is :-\n",cities_3)

# Example 2 :-

s1={1,2,5,6}
s2={3,6,7}
print("The set after symmetric_difference_update() method in s2 is :-\n",s2.symmetric_difference_update(s1))

# 7) difference() :-

# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_3=cities_1.difference(cities_2)
print("The set after difference() method in cities_1 is :-\n",cities_3)

# Example 2 :-

s1={1,2,5,6}
s2={3,6,7}
print("The set after difference() method in s2 is :-\n",s2.difference(s1))


# 8) difference_update() :-


# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_1.difference_update(cities_2)
print("The set after difference_update() method in cities_1 is :-\n",cities_3)

# Example 2 :-

s1={1,2,5,6}
s2={3,6,7}
print("The set after difference_update() method in s2 is :-\n",s2.difference_update(s1))


# 9) isdisjoint() :-

'''
# Checks if items of given set are present in another set.This method
# returns False if even atleast 1 item is present as they are not dis joint
# , else it returns True.
# '''

# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_3=cities_1.isdisjoint(cities_2)
print("The set is disjoint :- ",cities_3)

# Example 2 :-

s1={1,2,5,6}
s2={3,7}
print("The set is disjoint :-",s2.isdisjoint(s1))

# 10) issuperset() :-

'''
Checks if all the items present in a set are present in the other set
if present then returns True, else it returns False
'''

# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_3=cities_1.issuperset(cities_2)
print("The set is superset :- ",cities_3)

# Example 2 :-

s1={1,2,5,6}
s2={3,7}
print("The set is superset :-",s2.issuperset(s1))


# 11) issubset() :- 

'''
Checks if all the items of the ORIGINAL SET are present in the PARTICULAR
SET. It returns True if all the items are Present, else it returns False
'''

# Example 1 :-

cities_1={'Tokyo',"Madrid",'Berlin',"Delhi"}
cities_2={"Tokyo",'Seoul',"Kabul",'Madrid'}
cities_3=cities_1.issubset(cities_2)
print("The set is subset :- ",cities_3)

# Example 2 :-

s1={1,2,3,5,6,7}
s2={3,7}
print("The set is subset :-",s2.issubset(s1))


# 12) add() :- adds a single item to the set

# Example 1 :-

s1={22,32,37}
print("The s1 set is :- ",s1)
s1.add(77)
print("The update s1 is :- ",s1)


# 13) update() :- adds more than 1 items even items of another set,list,dictionary,tuple

# Example :-

s1={"Helsinki","Delhi",'Tokyo'}
s2=[22,33]
s3=(77,67)
s1.update(s2,s3)
print("The updated s1 is :-\n",s1)

# 14) remove() / discard():- 

'''
Both remove() and discard() removes item from the set but the difference 
is that :-
If i am trying to remove such an item which is not present in the set
then remove() method will raise an error but discard() method won't
'''

s1={"Harish",True,76,77.6}
print("Using remove() to remove an item which is present :-")
s1.remove(True)
print(s1)

# s1={"Harish",True,76,77.6}
# print("Using remove() to remove an item which is absent :-")
# s1.remove(False)
# print(s1)   # ---> KeyError: False

s1={"Harish",True,76,77.6}
print("Using discard() to remove an item which is present :-")
s1.discard(77.6)
print(s1)

s1={"Harish",True,76,77.6}
print("Using discard() to remove an item which is absent :-")
s1.discard(False)
print(s1) 
# Even i am trying to discard item which is not present still it is not displaying any error like remove() method


# 15) pop() :-

'''
This method removes last item from set but since set is unordered so 
i don't actually know which item is popped but i can know it if i assign
pop() method to a variable then printing that variable.
'''

s1={'Harish',77,7.87,True}
a1=s1.pop()
print("The popped item is :",a1)

# 16) del :-

# set_1={"Haria",True,33,7,9}
# print(set_1)
# del set_1
# print(set_1)   # ---> NameError: name 'set_1' is not defined

# 17) clear() :- just deletes all items in a set and make it an empty set

set_1={"Garia",22,2.7,True}
print(set_1)
set_1.clear()
print(set_1)

# 18) check if an item exists :-

info={'Carla',19,True,7.7}
if "Carla" in info:
    print("Carla is present")
else:
    print("Carla is not present")