'''

Create a program capable of displaying questions to the user like in KBC
Use list data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game

'''

sum=0
list=['a','b','c','d']
list_1=["When did India got independence ?",'1919','1927','1957','1947']
list_2=['What is capital of India ?',"Odisha","New Delhi","Maharashtra",'Bangkok']
print(list_1[0])
for i in range(0,4):
    print(list[i]+")",list_1[i+1])
a=input("Enter option number : ")
a=a.lower()
if a=='d':
    print("Correct answer")
    sum+=1000
else:
    print("Wrong answer")
print("Current amount =",sum)
print(list_2[0])
for i in range(0,4):
    print(list[i]+")",list_2[i+1])
b=input("Enter option number : ")
b=b.lower()
if b=='b':
    print("Correct answer")
    sum+=2000
else:
    print("Wrong answer")
print("Current amount =",sum)