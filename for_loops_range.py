for i in range(5): # ------> [0,5,0]
    print(i,end=' ')
print('\n')
for i in range(2,7): # -----> [2,7,0]
    print(i,end=" ")
print("\n")
for i in range(3,17,4): # -----> [3,17,4]
    print(i,end=" ")

'''
IN EVERY range() FUNCTION THERE ARE 3 PARAMETERS range(l,m,n)
l ----> starting value
m ----> value ends at (m-1)
n ----> [STEP DISTANCE] gap with which values will update from l to (m-1)
'''