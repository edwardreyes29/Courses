#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

# Indentation do not define scope of variables

if x < y:
    z = 112 # scope is still the same outside of this scope
    print('x < y: x is {} and y is {}'.format(x, y))
    print('line 2')
    print('line 3')
    print('line 4')
print('z is {}'.format(z)) # can still can still access z

x = 2
y = 2
if x > y:
    print('hello there')
elif x == y: # like elseif
    print('You are a bold one')
else:
    print('General Kenobi')

