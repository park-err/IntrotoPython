# Define the user's information as variables
weight = int(input("What is your weight in pounds: "))
print("Fill out the following information about your height.")
height_feet = int(input("First, feet: "))
height_inches = int(input("Now, inches: "))

# Calculations and conversion to determine the BMI
trueHeight = float((height_feet * 12) + height_inches)
userBMI = float(weight * (703 / (trueHeight ** 2)))

# Display the information to the user
print("Your BMI is", format(userBMI, '.1f'))
if userBMI > 25:
    print("You are considered overweight")
elif userBMI >= 18.5:
    print("You are considered to be an ideal weight")
else:
    print("You are considered underweight")
