# str='runningg'
# str_1=str[0]
# str_2=str[len(str)-1]
# print(str_1)
# print(str_2)
# if len(str)%2==0:
#     str_3=str[int(len(str)/2)-1]+str[int(len(str)/2)]
#     print(type(len(str)/2))
# else:
#     str_3=str[int((len(str)-1)/2)]
# print(str_1+str_3+str_2)

# 2nd :-

# str=input()
# i=int(input())
# s=str.replace(str[i-1],'')
# print(s)

# 3rd :-

# l=[-1,2,-2,0,4]
# l_max=l[0]
# l_min=l[0]
# for i in l:
#     if i>l_max:
#         l_max=l[i]
#     elif i<l_min:
#         l_min=i
# print(l_max,l_min,sep=" ")

# 4th :-
# l=(1,2,3,4,3,2,5,6,66,6,6,6)
# r=[]
# for i in l:
#     if i in r:
#         continue
#     if i not in r:
#         r.append(i)
# print(r)

# 5th :-

# k='*'
# for i in range(5,0,-1):
#     print(i*k)

# 6th :-

# for i in range(5):
#     print((i+1)*'#')

# 7th :-

# k=1
# for i in range(4):
#     for u in range(i+1):
#         print(k,end=' ')
#         k+=1
#     print()