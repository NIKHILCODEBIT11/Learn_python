'''

1) count() :- The count() method of Tuple RETURNS the number of times the 
given element appears in a tuple

'''

print("Output is given by using count() method")
tuple_1=(0,12,13,12,12,32,12,23,34,43,12)
a=tuple_1.count(12)
print("The count of",12,"in tuple is",a)

'''

2) index() :- The index() method RETURNS the index value of the first 
occurence of the given element from the tuple.

'''

print("Output is given by using index() method")
tuple_2=(0,12,45,54,566,56,"Harry",77)
b=tuple_2.index('Harry')
print("The index of the first occurence of 'Harry' is",b)

'''
EVEN I CAN USE index() METHOD IN SUCH A WAY THAT I CAN LOOK OUT FOR INDEX
OF AN ELEMENT IN IT'S FIRST OCCURENCE IN A SPECIFIED SLICED RANGE
'''

print("Output is given using index() in a sliced range")
tuple_3=(22,33,44,55,43,34,43,44,49)
c=tuple_3.index(43,5,7) # ---> It means look out for first occurence of 43
                        # ---> starting from 1t index going upto 6th index.
print("The index value of",43,"in range is",c)

# index() method raises value error if the element is not found in the tuple.

'''

3) len() :-  The len() method RETURNS the length of the tuple

'''

print("Output using len() method")
tuple_4=(22,32,34,444,56,67,766,765)
d=len(tuple_4)
print("The length of the tuple is",d)

# I can use all the elements of the list if i convert tuple into a list
