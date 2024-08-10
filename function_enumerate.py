'''

The enumerate function is a built-in function in python that allows me to
loop over a sequence(such as a list,tuple or string) and get the index
and value of each element in the sequence at the same time.

Here's a basic example of how it works :-

'''
fruits=['Apple','Orange',"Mango"]
for index,fruit in enumerate(fruits):
    print(index,fruit)


# Example 2 :-

marks=[12,33,44,23,77,67]
for index,mark in enumerate(marks):
    print(mark)
    if index==3:
        print('Performance need to be good')

# Example 3 :-   CHANGING THE START INDEX

'''
By default, the enumerate function starts the index at '0', but i can
specify a different starting index by passing it as an argument to the  
enumerate function.
'''

fruits=['Apple','Orange','pine apple']
for index,fruit in enumerate(fruits,start=2):
    print(index,fruit)

# Example 4 :-

marks=[12,33,43,37,77,67]
for marks,index in enumerate(marks,start=1):
    print(marks,")",index)
    if marks==3:
        print('Above marks is just passed here')
 

# Example 5 :- Below is an example with a tuple :-


colors=('Red','Green','Faint')
for index,colors in enumerate(colors):
    print(index,colors)

# Example 6 :- Below is an example with a string :-

s='Hello'
for index,s in enumerate(s):
    print(index,s)