#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
print('x is {}'.format(x))
print(type(x))
x = 7.0
print('x is {}'.format(x))
print(type(x))
x = 'hello' # There is no diff b/w "" and ''
print('x is {}'.format(x))
print(type(x))
x = True
print('x is {}'.format(x))
print(type(x))
x = None
print('x is {}'.format(x))
print(type(x))

# Multiline string [Type String]
x = '''

Hello there!
General Kenobi!
You are a bold one!

'''
print('x is {}'.format(x))
print('x is {}'.format(x.capitalize()))
print('x is {}'.format(x.upper()))

x = 'seven {} {}'.format(8, 9)
print('x is {}'.format(x))
print(type(x))

x = 'seven {1} {0}'.format(8, 9)
print('x is {}'.format(x))
print(type(x))

x = 'seven "{1:<4}" "{0:>4}"'.format(8, 9) # 1:<4 left adjust 4, 0:>4 right adjust 4
print('x is {}'.format(x))
print(type(x))

x = 'seven "{1:<04}" "{0:>04}"'.format(8, 9) # fills with zeros
print('x is {}'.format(x))
print(type(x))

# f string
a = 'eight'
b = 'nine'
x = f'seven {a} {b}' # f strings -> python 3.6 and after. Not positional, uses variable names
print('x is {}'.format(x))
print(type(x))

# f string
a = 'eight'
b = 'nine'
x = f'seven {a:<06} {b:>09}' # f strings -> python 3.6 and after. Not positional, uses variable names
print('x is {}'.format(x))
print(type(x))

# [Numeric Types]
x = 7 * 3.14159
print('x is {}'.format(x))
print(type(x))

x = 7 / 3 # returns a floating point number in python 3
print('x is {}'.format(x))
print(type(x))

x = 7 % 3 # returns remainder
print('x is {}'.format(x))
print(type(x))

# For computing, sacrifices accuracy for precision -> does arithmetic correctly to 17 decimal places
# But not accurate
# Accuracy is the true value of a calculation
# (!) Don't use floating points for money!
# The equation below needs to be 0 for money
x = .1 + .1 + .1 - .3 # expect this to be 0, not the case. Returns a very miniscule number.
print('x is {}'.format(x))
print(type(x))

# One work-around is to use a Decimal numeric type 
# Understanding Numeric types is very useful
from decimal import *
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))

# [Boolean Types]
x = 7 > 5
print('x is {}'.format(x))
print(type(x))

# special type None
# used to represent Absence of a value
x = None
print('x is {}'.format(x))
print(type(x))

if x:
    print('True')
else:
    print('False')

# Few things that evaluate to false, 0, None, False, empty string. Everything evaulates to true

x = 'x'
if x:
    print('True')
else:
    print('False')

x = 1
if x:
    print('True')
else:
    print('False')

x = 0
if x:
    print('True')
else:
    print('False')
print()

print('[type(& id()]')
#[type() & id()]
x = (1, 2, 3, 4, 5)
print('x is {}'.format(x))
print(type(x))

x = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x)) # Still tuple

# Check type of element in tuple
print(type(x[1]))
print(type(x[3]))

print('<<<<< compare x and y >>>>>>')
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print(type(x))
print(type(y))

# Will get two unique numbers -> two different objects
print(id(x)) 
print(id(y))
print(id(x[0]))
print(id(y[0]))
print(id(x[3]))
print(id(y[3]))

# check if same object
if x[0] is y[0]:
    print('Yes!')
else:
    print('No')

# Check if a particular object is a list or tuple with isinstance()
if isinstance(y, tuple):
    print('tuple')
elif isinstance(x, list):
    print("list")
else:
    print('no')
