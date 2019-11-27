#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
print(a)
print(b)
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b
    # a = b, and b = a + b

print() # line ending
