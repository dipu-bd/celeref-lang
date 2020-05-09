import math


def plus(*args):
    '''summation'''
    return sum(*args)


def minus(a, b):
    '''substract'''
    return a - b


def cross(*args):
    '''multiply'''
    return math.prod(*args)


def div(a, b):
    ''''division'''
    return a / b


def floordiv(a, b):
    '''interger division'''
    return a // b


def mod(a, b):
    '''modulus'''
    return a % b


def eq(*args):
    '''equal'''
    return len(set(args)) == 1


def neq(*args):
    '''not equal'''
    return len(args) == len(set(args))


def gt(a, b):
    '''greater than'''
    return a > b


def lt(a, b):
    '''less than'''
    return a < b


def geq(a, b):
    '''greater than or equal'''
    return a >= b


def leq(a, b):
    '''less than or equal'''
    return a <= b
