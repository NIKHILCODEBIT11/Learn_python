names='harish,param'
print(names[0:9])   #-------> IT WILL PRINT STARTING FROM 0th INDEX TO (9-1) INDEX.

# CONCEPT OF LENGTH OF A STRING :-
fruit="mango"
len_1=len(fruit)
print('Mango is a',len_1,'letter word.')

# PRINTING THE STRING OR PART OF STRING USING INDEXING :-

# METHOD-1 :-
print(fruit[0:4]) # -----> INCLUDES 0 BUT NOT 4.

# METHOD-2 :-
print(fruit[1:4]) # -----> INCLUDES 1 BUT NOT 4.

# METHOD-3 :-
print(fruit[:5]) # -----> BY DEFAULT IF I LEAVE THE 1ST PLACE VACCANT THEN IT IS FILLED AUTOMATICALLY BY 0.

# METHOD-4 :-
print(fruit[0:-3]) # -----> WHEREVER -( ) IS PRESENT THEN SIMPLY ADD LENGTH OF STRING TO THE -(INDEX) MENTIONED.
                            # LIKE len(fruit)-3.
# METHOD-5 :-
print(fruit[:len(fruit)-3]) # ------> NOTHING IS MENTIONED IN FIRST POSITION INDEX SO BY DEFAULT 0.

# METHOD-6 :-
print(fruit[-1:-3]) # ------> DOESN'T MAKE SENSE AS IN SIMPLE LANGUAGE I HAVE TO PRINT FROM INDEX 4 TO 2 BUT IT IS NOT HAPPENING.

# METHOD-7 :-
print(fruit[:]) # ------> AT LEFT OF ' : ' THE DEFAULT VALUE IS 0 AND AT THAT OF RIGHT OF ' : ' IS LEN(STRING).

# IMPORTANT EXAMPLE :-
# METHOD-7 :-
print(fruit[-3:-1])