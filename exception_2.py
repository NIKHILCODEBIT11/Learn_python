a=input("Enter a number : ")
print(f"Multiplication table of {a} is :-")
try:
    for i in range(10):
        print(f'{a}*{i}={int(a)*i}')
except Exception as e: # ---. I CAN'T WRITE AS   "exception as e"
    print(e)
print("Some imp code")
print("End of program")