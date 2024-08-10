file1 = open("see_3_try.txt", "w") 
lst = [] 
for i in range(3): 
	name = input("Enter the name of the employee: ") 
	lst.append(name + '\n') 
print(lst)
file1.writelines(lst) 
file1.close() 
print("Data is written into the file.") 