"""
This modules provides a number of important functions.

This code is free and open source software, distributed by the
GNU Public Licence (GPL 3.0).

Copyright: Mark Andrews, 2020

"""

x = [1, 2, 3, 4, 5]
y = dict(a = 1, b = 2, c = 3)
whoami = 'Mark Andrews'

class Person:

    """
    This class is a person object.
    """

    def __init__(self, name):
        'Initialize instance and assign name'
        self.name = name

    def greeting(self):
        'Return a greeting'
        print('Hello ' + self.name.capitalize())


def power(x, k = 3):
    """
    This function raises a value to the power of another
    value.
    """

    return x ** k


def square_root(x):

    """
    Return the square root of a number.
    """

    return x ** 0.5


if __name__ == "__main__":

    y = power(2)
    print(y)
