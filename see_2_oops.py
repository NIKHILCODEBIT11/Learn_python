class student():
    def __init__(self,name,l):
        self.name=name
        self.l=l
    def avg(self):
        # return (self.l[0]+self.l[1]+self.l[2])/3
        sum=0
        for i in self.l:
            sum+=i
        return sum/3
    @staticmethod #---> by using this keyword the function below will 
    # operate at class level not object level, so "self" paramter not 
    # required
    def hello():
        print('hello')
l1=[22,43,45]
s1=student('kar',l1)
'''hi'''
student.hello()
s1.hello()
print(s1.name)
print(s1.avg())