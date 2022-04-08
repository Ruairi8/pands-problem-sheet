# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the 
# one set of axes.
# Author: Ruairi McCool

# Parameters 'label' and 'markers' must be imported from cProfile and matplotlib. Matplotlib.pyplot is a useful 
# tool for outputting graphs. There are many functions contained with it that can be used to change style or 
# type of an output. 'Numpy' is a library consisting of multidimensional array objects, and a collection of
# routines for processing those arrays. Numpy allows you to use maths and logical operations on arrays. The 'as'
# keyword allows you to create a shorter psuedoname:
# https://www.mygreatlearning.com/blog/python-numpy-tutorial/
from cProfile import label
from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

# Defining three functions, with x as a parameter:
def f(x):
    return x
def g(x):
    return x ** 2
def h(x):
    return x ** 3

# np.arange returns evenly spaced values within a given interval using a certain stepsize:
# https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange
x1 = np.arange(0, 4, 1)
# Assigning colors y=yellow, b=blue, r=red to the graph lines.
plt.plot(f(x1), 'y', linewidth=2.5, marker="d", label='f(x1)')
plt.plot(g(x1), 'b', linewidth=2.5, marker="d", label="g(x1)")
plt.plot(h(x1), 'r', linewidth=2.5, marker="d", label="h(x1)")
plt.legend(loc="upper left")
plt.title("plottask.py")
# Ticks distribution on x-axis:
plt.xticks(np.arange(0, 4, 1))
plt.grid(True)
# Minimum & maximum ticks on x and y axes:
# https://towardsdatascience.com/plot-in-python-with-matplotlib-step-by-step-dd69f2e9175a
plt.axis(xmin = 0, xmax = 3.1, ymin = 0, ymax = 28) 
# Giving the y-axis labels for each line plot:
plt.ylabel('f(x) = x ' + '\ng(x) = x2 ' + '\nh(x) = x3')
# Nothing will output when this program is run without using .show():
plt.show()