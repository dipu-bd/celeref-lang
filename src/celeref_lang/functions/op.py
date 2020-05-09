import math


def plus(*args):
    '''
    plus(*args) -> number
    Same as `sum(*args)`

    Add arbitrary number of arguments'''
    return sum(*args)


def minus(a, b):
    '''
    minus(a, b) -> number
    Same as `a - b`

    Substract first number from second'''
    return a - b


def cross(*args):
    '''
    cross(*args) -> number
    Same as `math.prod(*args)`

    Multiply arbitrary number of arguments'''
    return math.prod(*args)


def div(a, b):
    '''
    div(a, b) -> number
    Same as `a / b`

    Floating point division of two numbers'''
    return a / b


def floordiv(a, b):
    '''
    floordiv(a, b) -> number
    Same as `a // b`

    Interger division between two numbers'''
    return a // b


def mod(a, b):
    '''
    mod(a, b) -> number
    Same as `a % b`

    Find the modulus of two numbers'''
    return a % b


def eq(*args):
    '''
    eq(*args) -> bool
    Same as `len(set(args)) == 1`

    Check if all arguments are equal'''
    return len(set(args)) == 1


def neq(*args):
    '''
    neq(*args) -> bool
    Same as `len(args) == len(set(args))`

    Check if no arguments are unique
    '''
    return len(args) == len(set(args))


def gt(a, b):
    '''
    gt(a, b) -> bool
    Same as `a > b`

    Check if first argument is greater than the second
    '''
    return a > b


def lt(a, b):
    '''
    lt(a, b) -> bool
    Same as `a < b`

    Check if first argument is less than the second'''
    return a < b


def geq(a, b):
    '''
    geq(a, b) -> bool
    Same as `a >= b`

    Check if first argument is greater than or equal to the second'''
    return a >= b


def leq(a, b):
    '''
    leq(a, b) -> bool
    Same as `a <= b`

    Check if first argument is less than or equal to the second'''
    return a <= b
