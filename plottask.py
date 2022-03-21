# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x
def g(x):
    return x ** 2
def h(x):
    return x ** 3

# np.arange returns evenly spaced values within a given interval. https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange
x1 = np.arange(0, 4, 1)
plt.plot(f(x1), 'y', g(x1), 'b', h(x1), 'r')
plt.xticks(np.arange(0, 4, 1))
plt.axis(xmin = 0, xmax = 4, ymin = 0, ymax = 30) # https://towardsdatascience.com/plot-in-python-with-matplotlib-step-by-step-dd69f2e9175a
plt.ylabel('f(x) = x ' + '\ng(x) = x2 ' + '\nh(x) = x3')
plt.show()