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


'''
Since, in #7 at 4th line i have written    print(len(str.center(50)))   but i am operating with str4 still i am not getting any error because in vs code i have written all methods in a single file where i already had defined a striing named str.
So now when i run   print(len(str.center(50)))   then i am simply considering str with center gap of 50 spaces.

{{{{{{{{{{ IT DOES NOT MEAN THAT THE str IS CHANGED TO SUCH A STRING WHICH HAS CENTER SPACE GAP OF 50 SPACES RATHER IT SIMPLY MEANS THAT IF I WILL ASSIGN THAT METHOD TO SOME NEW STRING THEN IT WILL JUST COPY SUCH STRING TO THE NEW STRING BUT str4 WON'T BE CHANGED AT ALL AS STRINGS ARE IMMUTABLE.
'''

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

# 10 find()
str7="He's name is Haria. He is an honest man"
print("The first occurence of \"is\" is",str7.find("is"))
print("The 1st occurence of \"was\" is",str7.find("was"))

# 11 index()
str8="He's name is Haria. He is an honest man"
print("The index value of \"is\" is",str8.index("is"))
# print("The index value of \"was\" is",str8.index("was"))

# 12 isalnum()
str9="Welcometomyworld"
str_9="Welcome to my world!!!"
print("The string in str9 is alpha numeric :",str9.isalnum())
print("The string in str_9 is alpha numeric :",str_9.isalnum())

# 13 isalpha()
str10="Welcometomyworld1"
str_10="Welcome to my world!!!"
print("The string in str10 is alpha :",str10.isalpha())
print("The string str_10 is alpha :",str_10.isalpha())

# 14 islower()
str11="welcome to my world"
str_11="weLcome to my world"
print("The string str11 is lower :",str11.islower())
print("The string str_11 is lower :",str_11.islower())

# 15 isprintable()
str12="Hello, welcome to my world"
str_12="Hello, welcome to my world\n"  # ----> '\n' is not printable as it is an escape sequence.
print(str12)
print(str_12)
print("The string str12 is printable :",str12.isprintable())
print("The string str_12 is printable :",str_12.isprintable())

# 16 isspace()

'''
-------> The isspace() method ***** RETURNS True ONLY AND ONLY IF THE 
STRING CONTAINS WHITE SPACES {{{ THAT MEANS WHOLE STRING WITH ONLY SPACES.}}}, ELSE RETURN False *******

-------> USING ***** SPACE BAR ***** OR ***** Tab *****
'''

str13="hello_running!w ild"
str_13="    "
print("The string str13 has space :",str13.isspace())
print("The string str_13 has space :",str_13.isspace())

# 17 istitle()
str14="Hello it is Your DAY"
str_14="Hello It Is Your Day"
print("The string str14 is title :",str14.istitle())
print("The string str_14 is title :",str_14.istitle())

# 18 isupper()
str15="MY NAME IS HARI!!!A!!!"
str_15="MY NAME IS HARia!!!"
print("The string str15 is upper :",str15.isupper())
print("The string str_15 is upper :",str_15.isupper())

# 19 startswith()
str16="Hello my name is haria"
print("The string str16 starts with 'He' :",str16.startswith("He"))
print("The string str16 starts with 'he' :",str16.startswith('he'))

# 20 swapcase()
str17="Hello my NAme is !!! H@Ari^^a"
print("The string str17 in swapcase is :",str17.swapcase())

#21 strip()
str18="   Silvery spoon "
print("The string str18 after strip is :"+str18.strip())
