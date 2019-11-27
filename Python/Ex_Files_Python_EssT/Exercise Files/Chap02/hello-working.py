#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
x = 42
print('Hello, World. {}'.format(x))

print('Hello there. %d' % x) # will be deprecated
#.format is a method of String object itself
# ust format method

# interpolation and format strings
print(f'Hello, World. {x}') # f for format