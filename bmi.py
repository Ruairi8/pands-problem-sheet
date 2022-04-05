# A program that calculates someone's Body Mass Index (BMI).
# Author: Ruairi McCool

# The input() function converts a line to a string & returns it. Here we need the user to input an integer.
# The int() function is needed to force the user to input an integer. https://www.geeksforgeeks.org/python-3-input-function/
height = int(input("Enter height in cm: "))
weight = int(input("Enter weight in kg: "))

# How body mass index is calculated. In Python a double asterisk means 'to the power of'.
Body_Mass_Index = weight / (height) ** 2

# Height is needed in meters so dividing height by one hundred. Also setting the formula equal to a variable (BMI).
# Then storing the variable in 'result' by using a comparator operator equal sign:
BMI = weight / (height/100) ** 2
result = BMI

# String format() method to reduce the output to two decimal places.
# https://jakevdp.github.io/WhirlwindTourOfPython/14-strings-and-regular-expressions.html
print("The BMI is (kg/m2) {:.2f}".format(result))
