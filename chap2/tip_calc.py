# In this project, I'll be creating a tip calculator. This program will be able to calculate how much each person should pay if group of friend decide to go eat out. 
# 

# DATA COLLECTION: 

# Introduction
print("Welcome to the tip calculator")


# Ask the use to enter the total of the bill
total_bill = float(input("Enter the total amount of the bill: $"))


# Ask the user for percentage of the tip. 
tip = int(input("What perecentage of tip would you like to add?: 10, 12,  or 15? "))

# Ask the user how many people is the bill going to split amongst? 
partcipants = int(input("Enter the number of partciptants: "))



# OUTPUT:

# Variable will calculate input of tip by dividing it by 100 and the times it with the total of the bill and then add it. 
bill_with_tip = tip / 100 * total_bill + total_bill

# Get result for per person 
total_bill = bill_with_tip / partcipants


# final amount with 2 decimal plades
# final_amount = round(total_bill[2])
final_amount = round(total_bill, 2)
final_amount = "{:.2f}".format(total_bill)
# final print
print(f"Each partcipant should pay ${final_amount}")