a=input('Enter a number : ')
print(f'Multiplication table of {a} is :- ')
try:
    for i in range(10):
        print(f'{a}*{i+1}={int(a)*i}')
except:
    print('Invalid input')
print("Some imp lines of code")
print("End of program")