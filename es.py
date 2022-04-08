# A program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line
# Author: Ruairi McCool

# https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python
import sys

# 'sys.argv[1]' will be the first argument in the command line, argv[0] is not used here because it is always
# the Python filename:
filename = sys.argv[1]
a = 0
# https://www.sanfoundry.com/python-program-read-file-counts-number/
# "rt" is used to specify reading a text. "with open" is used to read/write in a file:
with open(filename, "rt") as f:
# This will break down the text in the file (f) into separate lines:
    for line in f:
# Separating each word in each line using .split() method. Indentation used because the words are 'in' the lines:
        words = line.split()
# I want to do something with every element in the split line, here every element is a word (i). If 'words' was empty,
# the statement at the next level of indentation would not execute:
        for i in words:
            for letter in i:
                if (letter == 'e'):
# a += 1 is the equivalent of  a = a + 1. This will add 1 to a for every letter that is an e in the file:
                    a += 1
# Print statement should not be inside the for or if loops if we want to output a single value. Otherwise,
# there will be an output for the number of 'e's in each line for example, before it outputs the total for
# the file.
    print(a)