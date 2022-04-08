# A program that takes in a positive floating point number as input and outputs an approximation of it's 
# square root.
# Author: Ruairi McCool


# https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
# 'def' keyword is used to define a function: 
def newtonsqrt(n):
# Defining mathematical variables using the equal sign:
    sqRoot = 0.5 * n
    sqRoot2 = 0.5 * ((sqRoot + n) / sqRoot)
# A 'while' loop continues to execute as long as a certain condition is true, otherwise the process breaks out
# of the loop and moves, in this case, down to the return statement on line 16: 
    while sqRoot2 != sqRoot:
        sqRoot = sqRoot2
        sqRoot2 = 0.5 * ((sqRoot + n) / sqRoot)
    return sqRoot

# 'float' method forces the used to enter a floating point number:
user = float(input("Please enter a positive number: "))
# String formatting, '1f' will return an output floating point number with 1 number after the decimal.
print("The square root of {} is approx. {:.1f}".format(user, newtonsqrt(user)))