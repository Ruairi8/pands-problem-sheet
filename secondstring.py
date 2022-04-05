# A program that asks the user to input a string and outputs every
# second letter in reverse order. 

# Author: Ruairi McCool

sent = input("Please enter a sentence: ")
# A negative step number allows
# you to count from the end of a string to the beginning.
# "This is extended slice syntax. It works by doing [begin:end:step] - 
# by leaving begin and end off and specifying a step of -1, it reverses a string."
# https://stackoverflow.com/questions/931092/reverse-a-string-in-python?rq=1
revSent = sent[::-2]
print(revSent)


