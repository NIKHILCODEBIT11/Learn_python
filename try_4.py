class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"The name is {self.name} and salary is {self.salary}")
a=employee('harry',12)
a.display()