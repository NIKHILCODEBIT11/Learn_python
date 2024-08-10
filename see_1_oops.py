class student():
    def __init__(self,Name,marks):
        self.name=Name
        self.marks=marks
    def hello(self):
        print('hi',self.name)
s1=student('har',66)
print(s1.name,s1.marks)
s2=student('er',33)
print(s2.name,s2.marks)