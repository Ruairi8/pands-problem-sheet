# A program that asks the user to input a string and outputs every
# second letter in reverse order. 

# Author: Ruairi McCool

x = input("Please enter a sentence: ")
# Slice take in three values - start, stop, step. A negative step number allows
# you to count from the end of a string to the beginning.
# A colon denotes the entire string.
y = x[::-2]
print(y)


