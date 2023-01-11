# Python If and Else
#
# These conditions can be used in several ways, most commonly in "if statements" and loops.
# If statement, without indentation (will raise an error):


# Python supports the usual logical conditions from the mathematics

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


# Example of if statement but using 'if' keyword

# a = 23
# b = 2023

# if b > a:
#     print("b is greater than a")


# elif keyword means, 'if the previous conditions were not true, then try this condition'

# a = 29
# b = 29

# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")



# else keyword means, if the conditional expression in the if statement resolves to 0 or a FALSE value.
# a = 50
# b = 25

# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#   print("a is greater than b")



# Examlpe: ask user if they are old enough to drive

print("Welcome to AI-Car")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive")
else:
  print("Sorry you are not old enough drive")