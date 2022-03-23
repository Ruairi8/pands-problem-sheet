# A program that takes in a positive floating point number as input and outputs an approximationof it's 
# square root.
# Author: Ruairi McCool


# https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
def newtonsqrt(n):
    sqRoot = 0.5 * n
    sqRoot2 = 0.5 * ((sqRoot + n) / sqRoot)
    while sqRoot2 != sqRoot:
        sqRoot = sqRoot2
        sqRoot2 = 0.5 * ((sqRoot + n) / sqRoot)
    return sqRoot

user = float(input("Please enter a positive number: "))
print("The square root of {} is approx. {:.1f}".format(user, newtonsqrt(user)))