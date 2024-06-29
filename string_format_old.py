# 1) METHOD 1 :-

a1="Hey my name is {} and i am from {}"
a1_1=a1.format('Harish',"India") 
print(a1_1) # can also be written as print(a1.format("Harish","India"))


# 2) METHOD 2 :-

a2='Hey my name is {0} i am from {3} which is in {4} and i am {1} years old and i am {2}'
print(a2.format('Harish',12,"good",'New delhi',"India"))

'''
 The problem in method 2 is that i will have to check so many index 
 values for writing printing statement
'''

# 3) METHOD 3 :-

txt="For only {price:.7f} ruppees"
print(txt.format(price=49.2342008995))

# 4) METHOD 4 :-

txt_1="For only {:.7f} ruppees"
print(txt_1.format(49.32634562873))