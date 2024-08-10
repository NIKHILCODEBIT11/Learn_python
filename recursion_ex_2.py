# FIBONACCI SERIES :-
l=[]
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)   #   return fibo(n-2)+fibo(n-1)
n=int(input("Enter number of terms required in fibonacci : "))
m2=fibo(n)
a2='in'
for i in range(1,n+1):
    # print(fibo(i))
    a_i=fibo(i)
    l.append(a_i)
print(l)
print(f'The last term {a2} fibonacci series for {n} is',m2)