str="!!!Haria!!!!"

# 1) UPPER()
print(str.upper())

# 2) LOWER()
print(str.lower())

# 3 rstrip()
print(str.rstrip("!"))

# 4 replace()
print(str.replace("a","M"))
str1="Silver Spoon"
print("If the word to be replaced is not present "+str1.replace("silver","gig"))
print("If the word to be replaced is present "+str1.replace("Silver","gig"))

# 5 split()
str2="!!!Haria !! !!!!! harr !!!y!!!"
print(str2.split(" "))  # -----> IT MEANS SPLIT THE STRING INTO LIST ELEMENTS WHEREVER THERE IS SPACE.

# 6 capitalize()
str3="introDUctIon TO javaScRipT"
str_3=str3.capitalize()
print(str_3)

# 7 center()
str4="welcome to the console"
print(len(str4))
print(str4.center(50))
print(len(str.center(50)))

# 8 count()
str5="!!!Harry!! harry* Harry $!2harry^&"
print("The value of count is",str5.count("harry"))

# 9 endswith()
str6="Welcome to the console!!@"
str_6=str6.endswith("!@")
print(str_6)

str__6=str6.endswith("to",4,10) # ----> It will check from 4th index to 
print(str__6)                    # (10-1)=9th index whether it ends with 
                                # "to" or not if yes then True else False 