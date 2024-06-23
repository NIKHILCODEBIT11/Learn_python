# Table of any number

n=int(input("Enter the number :"))
k=int(input("Enter upto which term table to be skipped :"))
l=int(input("Enter the range :"))
for i in range(l):
    print(n,'*',i,'=',n*i)
    if(i==k):
        break