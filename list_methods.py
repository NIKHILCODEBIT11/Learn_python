# 1) append() :- This method adds new items to the original list.

l=[1,3,7,67]
print(l)

#  l.append(91,93) ----> append methods takes one and only one argument

l.append(92)
print(l)


# 2) sort() :- This method sorts the items of list in ascending order. The original list is updated.

l1=[1,33,21,24,43,77]
l1_1=['blue',"green","violet",'red',"saffron"]
print(l1)
l1.sort()
print(l1)
print(l1_1)
l1_1.sort()
print(l1_1)

# ----> Even i can print list items in descending order.


l1.sort(reverse=True)
print(l1)

# 3) reverse() :- This method reverses the order of the list and  the original list is updated.
l2=[22,23,34,33]
print(l2)
l2.reverse()
print(l2)