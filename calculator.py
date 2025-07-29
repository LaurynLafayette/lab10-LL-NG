"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by 0")

def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        raise ValueError("Invalid Value")

def exp(a, b):
    return a ** b