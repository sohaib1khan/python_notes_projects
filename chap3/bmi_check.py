# This Python script will calculates a person's Body Mass Index (BMI) based on their height and weigh

# First prompt the user to enter their height and weight and then convert the input to a float number.

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI using the formula weight / height^2
bmi = weight / (height ** 2)

# here, check the value of bmi and print an appropriate message based on the range of bmi values
if bmi < 18.5:
    print(f"Your BMI is {bmi}, which is considered underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, which is considered normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, which is considered overweight.")
else:
    print(f"Your BMI is {bmi}, which is considered obese.")