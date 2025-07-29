"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError:
        raise ValueError("Input value 'a' cannot be negative.")

def hypotenuse(a, b):
    result = math.hypot(a,b)
    return result


def add(a, b):
    return a + b
