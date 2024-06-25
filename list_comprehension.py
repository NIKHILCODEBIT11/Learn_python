lst_1=[item for item in range(4)]
print(lst_1)

lst_2=[i*i*i for i in range(7)]
print(lst_2)

lst_3=[i*i for i in range(7) if i%3==0]
print(lst_3)

'''

EXAMPLE 1 :-

Accepts items with the small letter 'o' in the new list.

'''

names=['Rohan','marry',"soham"]
name_with_o=[name for name in names if "o" in name]
print(name_with_o)


'''

EXAMPLE 2 :-

Accepts items which have more than 4 letters

'''

name=['saraya',"sarah",'bruno',"hi","rier","jis"]
name_with_4_let=[item for item in name if len(item)>=4]
print(name_with_4_let)