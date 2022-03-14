# A program that asks the user to input a positive integer and outputs successive values of a calculation.
# Have the program end if the current value is one.
# Author: Ruairi McCool

def collatz(num):
    arr = []
    user = int(input("Please enter a positive integer: "))
    while user != 1:
        if user % 2 == 0:
            arr.append(user / 2)
        else:
            arr.append((user * 3) + 1)
# Matching indentation levels are part of the same block of code. Python follows the "off-side" rule convention
# After the end of an if statement is reached, execution goes to the first statement having a lesser indentation
# level. So, the code on the line below is guarenteed to be executed. https://realpython.com/python-conditional-statements/#python-its-all-about-the-indentation
    
print(arr)