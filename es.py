"""A program that reads in a text file & outputs the number of e's it contains. The program should take the 
filename from an arguement on the command line."""
# Author: Ruairi McCool

import sys
print(sys.argv)
with open(sys.argv[0]) as f:
    for x in f:
        x = x.count('e')
        print(x)
print("Hello I'm in es.py")