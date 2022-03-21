# A program that asks the user to input a positive integer and outputs successive values of a calculation.
# Have the program end if the current value is one.
# Author: Ruairi McCool

# https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence
def collatz_sequence(x):
# Creating an empty array which I will use the function to output the sequence, and later iterate through
# the array.
    arr = []
    if x < 1:
       return []
    while x > 1:
# Matching indentation levels are part of the same block of code. Python follows "off-side" rule convention.
# After the end of an if statement is reached, execution goes to the 1st statement with a lesser indentation
# level. 
# https://realpython.com/python-conditional-statements/#python-its-all-about-the-indentation
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1 
       arr.append(x)    
    return arr

user = int(input("Enter number: "))
for y in collatz_sequence(user):
    # https://stackoverflow.com/questions/2440692/formatting-floats-without-trailing-zeros
    print("{:.2f}".format(y).rstrip("0").rstrip("."), end=" ")



