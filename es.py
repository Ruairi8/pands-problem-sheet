# A program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line
# Author: Ruairi McCool

import sys

filename = sys.argv[1]
a = 0
# "rt" is used to specify reading a text. "with open" is used to read/write in a file.
with open(filename, "rt") as f:
# Breaking down the text into separate lines:
    for line in f:
# Separating each word in each line using .split() method. Indentation used because the words are 'in' the lines:
        words = line.split()
# I want to do something with every element in the split line, here every element is a word (i). If 'words' was empty,
# the statement at the next level of indentation would not execute:
        for i in words:
            for letter in i:
                if (letter == 'e'):
# a += 1 is the equivalent of  a = a + 1. This will add 1 to a for every letter that is an e in the file.
                    a += 1
# Print statement should not be inside the for or if loops if we want to output a single value. Otherwise,
# there will be an output for the number of 'e's in each line for example, before it outputs the total for
# the file.
    print(a)