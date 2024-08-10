# i = 1
# f = open('see_ex_2.txt')
# for line in f.readlines():
#     if i % 2 == 0 :
#         print(line)
#     i += 1

with open('see_ex_2.txt','r') as f:
    for i in range(len(f.readlines())):
        if i%2!=0:
            print(f.readline())
            print(i)
        if i%2==0:
            print(f.readline())
            print(i,'is')