# A program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line
# Author: Ruairi McCool

import sys

filename = sys.argv[1]
a = 0
# "rt" is used to specify reading a text. 
with open(filename, "rt") as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter == 'e'):
                    a += 1
# Print statement should not be inside the for or if loops if we want to output a single value. Otherwise,
# there will be an output for the number of 'e's in each line for example, before it outputs the total for
# the file.
    print(a)