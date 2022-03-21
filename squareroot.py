# A program that takes a positive floating point number as input and outputs an approximation of its square
# root.
# Author: Ruairi McCool

from sqlalchemy import Float

num = float(input("Please enter a positive integer: "))
if num < 0:
    try:
        print(float(input("It must be a positive floating point number: ")))
    except ValueError:
        print(float(input("This isn't a number! Enter a positive floating-point number: ")))


def sqrt(num):
    sqrt1 = 0.5 * num
    sqrt2 = 0.5 * (sqrt1 + num/sqrt1)
    # Could become an infinite loop!
    while abs(sqrt1 -sqrt2) > 0.001:
        sqrt2 = 0.5 * (sqrt1 + num/sqrt1)
    return sqrt2

sqrt1 = 0.5 * num
sqrt2 = 0.5 * (sqrt1 + num/sqrt1)
print("The square root of {} is approx. {}".format(num, sqrt2))

