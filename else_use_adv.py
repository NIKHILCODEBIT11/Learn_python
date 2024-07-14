print('Example 1')
# Example 1 :-

for i in range(5):
    print(i)
else:
    print('Sorry no i')

print("\nExample 2")
# Example 2 :-

for i in []:  # Empty list
    print(i)
else:
    print('Sorry no i')

print('\nExample 3')
# Example 3 :-    ( v.v.v.v important )

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print('sorry no i')

'''

Reason - Since in above example 4 before the execution of 'else' block
 the 'for' loop breaks that's why due to incomplete execution of 
'for' loop 'else' block was not executed.

'''
print('\nExample 4')
# Example 4 :-  ( Above concept using while loop )

i=0
while i<7:
    print(i)
    i+=1
    if i==4:
        break
else:
    print('Sorry no i')

print('\nExample 5')
# Example 5 :-

for x in range (5) :
    print('Iteration no. {} in for loop'.format(x+1))
else:
    print('Else block in loop')
print("Out of loop")