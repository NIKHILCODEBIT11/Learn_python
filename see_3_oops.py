class complex:
    def __init__(self,real,img):
        self.real=real
        self.imag=img
    def show(self):
        print(self.real,'+',self.imag,'i')
    def __add__(self,self_1):
        new_real=self.real+self_1.real
        new_imag=self.imag+self_1.imag
        return complex(new_real,new_imag)
    
c1=complex(2,3)
c2=complex(-3,-7)
c1.show()
c2.show()
c3=c1+c2
c3.show()