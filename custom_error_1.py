salary=int(input('Enter salary amount : '))
if not 2000<salary<5000:
    raise ValueError('Not a valid salary')

# ---> When i am raising error then, I can't define as :-  ValueError as e1 and then print(e1)