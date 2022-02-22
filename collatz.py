# A program that asks the user to input a positive integer and outputs successive values of a calculation.
# Have the program end if the current value is one.
# Author: Ruairi McCool


arr = []
user = int(input("Please enter a positive integer: "))
if user % 2 == 0:
    arr.append(user / 2)
else:
    arr.append((user * 3) + 1)

print(arr)



