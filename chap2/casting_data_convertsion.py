# # Python Casting 
# # There may be times when you want to specify a type on to a variable. This can be done with casting
# # nt() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# # float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# # str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


# # int:
# x = int(1)
# y = int(2.8)
# z = int("3")
# print(x)
# print(y)
# print(z)


# # float:
# x = float(1)
# y = float(2.8)
# z = float("3")
# w = float("4.2")
# print(x)
# print(y)
# print(z)
# print(w)


# # Strings: 
# x = str('s1')
# y = str(234)
# w = str(6.094)
# print(x)
# print(y)
# print(w)

# # convert strings to integers
# num_of_characters = len(input("what is your name? "))

# # need to convert strings to integers
# # name_characters = str(num_of_characters)
# # print("Your name has " + name_characters + " characters.")

# or another example
# # print("Your name has %d characters." % num_of_characters)


a = str(123)
print(a)
print(type(a))

print(70 + float("100.5")) # what is the result?

print(str(70)+ str(100)) # what  is the result?
