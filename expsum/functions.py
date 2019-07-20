import numpy as np


def func1(n, a, b, c):
    """
    Function 1
    """
    fn = n / a + n**2 / b + n**3 / c
    return fn


def func2(n, a):
    """
    Function 2
    """
    fn = np.log(n) + n**2 / a
    return fn


def func3(n):
    """
    Function 3
    """
    fn = np.log(n)**4.1
    return fn


def func4(n, a):
    """
    Function 4
    """
    fn = (np.log(n))**a
    return fn


def func5(n, a, b):
    """
    Function 5
    """
    fn = np.log(n) + n**2 / a + n**3 / b
    return fn


def func6(n, a):
    """
    Function 6
    """
    fn = np.sqrt(n) / a
    return fn


def func7(n, a):
    """
    Function 7
    """
    fn = np.sqrt(n ** 3) / a
    return fn
