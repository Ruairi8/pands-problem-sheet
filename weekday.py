# A program that outputs whether or not today is a weekday.
# Author: Ruairi McCool

# Datetime module included classes to manipulate dates & times. https://docs.python.org/3/library/datetime.html
from datetime import datetime
# 
result = datetime.today()
# Get the day number using the built-in python weekday() function, it starts with monday at 0. https://poopcode.com/check-day-weekday-weekend-python/
if result.weekday() > 4:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")


