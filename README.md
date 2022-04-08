
## Pands Problem Sheet Solutions

<p>A weekly task was given as part of the Programming and Scripting module. Solutions using the Python<br> programming language are included, comments on the code and references pointing to where some of ideas for the code was obtained.</p>


1. A program that calculates a persons body mass index.
- The user is asked to input height and weight, these values are entered in a formula to output the BMI.

- https://www.geeksforgeeks.org/python-3-input-function/
- https://jakevdp.github.io/WhirlwindTourOfPython/14-strings-and-regular-expressions.html


2. A program that asks a user to input a string, & outputs every second letter in reverse order.
- The code starts at the end of the string, and pops off every second letter from there.

- https://stackoverflow.com/questions/931092/reverse-a-string-in-python?rq=1


3. A program that asks a user to input a positive integer and outputs the succesive vales of the following<br>
   calculation: At each step calculate the next value by taking the current value and, if it is even<br>
   divide by two, if it is odd, multiply it by three and add one. Have the program end when the current<br>
   value is one.
- A function that contained an if else statement was created to output what is known as a Collatz series.
- Varioustring methods were used to tidy up the output.

- https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence
- https://realpython.com/python-conditional-statements/#python-its-all-about-the-indentation
- https://stackoverflow.com/questions/2440692/formatting-floats-without-trailing-zeros


4. Write a program that outputs whether or not today is a weekday.
- This involved importing a 'built-in' module called 'datetime'. There are many built-in modules in Python 
- that allow one to carry out many tasks that otherwise would not be possible. 

- https://docs.python.org/3/library/datetime.html
- https://poopcode.com/check-day-weekday-weekend-python/


5. Write a program that takes a positive floating-point number as input, and outputs an approximation of its 
   square root.
- Here I defined a function and used a while loop to performs calculations and output the result using 
- 'return'. String formatting was used to make the output look clearer.

- https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method


6. A program that counts the number of 'e's in a file.
- This was a new area of Python that explored reading and writing to a file and using the built-in os module
- to allow the user to output what is in a file from a command line.
- https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python
- https://www.sanfoundry.com/python-program-read-file-counts-number/


7. A program that displays a line graph of three different functions.
- This involved exploring an area of Python used to get graphical outputs and using different Python syntax
- and methods on the built-in mathplotlib.pyplot module to adjust the line graph.

- https://www.mygreatlearning.com/blog/python-numpy-tutorial/
- https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange
- https://towardsdatascience.com/plot-in-python-with-matplotlib-step-by-step-dd69f2e9175a