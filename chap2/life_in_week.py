# Calculate how many weeks in life left 

# Capture user age 
age = input("How are you right now?: ")

# Convert user age into an int/number 
age_as_int = int(age)

# calculate number of years left out the age of 90. assuming that we'll live by 90


years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12


# For output, make it into a var and then print or print the whole statement 
# f"You have {days_remaining} days, {weeks_remaining}, and {months_remaining} left "

# print(f"You have {days_remaining} days, {weeks_remaining}, and {months_remaining} months left until your expire.... better get working on your bucket list now! ")

# or

final_result = f"You have {days_remaining} days, {weeks_remaining}, and {months_remaining} months left until your expire.... better get working on your bucket list now! "
print(final_result)