# A program that asks the user to input a positive integer and outputs successive values of a calculation.
# Have the program end if the current value is one.
# Author: Ruairi McCool

# https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence
def collatz_sequence(x):
# Creating an empty array which I will use the function to output the sequence, and later iterate through
# the array:
    arr = []
    if x < 1:
# 'return' here sends an empty array back to the caller:
       return []
    while x > 1:
# Matching indentation levels are part of the same block of code. Python follows "off-side" rule convention.
# After the end of an if statement is reached, execution goes to the 1st statement with a lesser indentation
# level:
# https://realpython.com/python-conditional-statements/#python-its-all-about-the-indentation
       if x % 2 == 0:
# 'if-else statement'. When if is true, the indented line is executed on the next line, otherwise the indented
# line under 'else:' is executed:
         x = x / 2
       else:
         x = 3 * x + 1 
       arr.append(x)  
# Return statement to return the resulting array back to the caller: 
    return arr

user = int(input("Enter number: "))
for y in collatz_sequence(user):
    # https://stackoverflow.com/questions/2440692/formatting-floats-without-trailing-zeros
    print("{:.2f}".format(y).rstrip("0").rstrip("."), end=" ")



