# My solution to the question from week 2
# Author: Ruairi McCool

# The int() class is required for the input values.
height = int(input("Enter height in cm: "))
weight = int(input("Enter weight in kg: "))

# How body mass index is calculated
Body_Mass_Index = weight / (height)**2

# Height is needed in meters so diving height by one hundred
BMI = weight / (height/100) ** 2
result = BMI

# String format() method 
print("The BMI is {} kg/m2".format(result))
print("The BMI is {} kg/m2".format(result))
