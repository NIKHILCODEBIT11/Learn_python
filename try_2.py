def appl(fx,val):
    return fx(val)
double=lambda x:x*x
triple=lambda x:x**3

appl_1=lambda x:appl(triple,x)
avg=lambda x:(lambda x:(x**3))

print(double(2))
print(triple(2))
print(appl_1(4))
print(avg(6))
print(appl(double,9))