countries=('spain',"Russia","India",'England',"Germany")
temp=list(countries)
temp.append('Italy')
temp.pop(3) # ---> Always give index value only
            # ---> pop() is used for removing item or element from list
temp[2]="Finland"
print(countries)

# If i can't change tuple then how am i replacing tuple anmed countries to a new tuple with same name in below.
countries=tuple(temp)
print(countries)