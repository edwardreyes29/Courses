#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

# Can still call methods on strings
print('Hello, World'.upper())
print('Hello, World'.swapcase())
print('Hello, World. {}'.format(42 * 7))

print("""
    Hello,
    World.
    {}
    """.format(42 * 8))

# First class objects, everything works above on strings because strings are first class
# objects in python

s = 'Hello, World'
print(s.upper())
s = 'Hello, World {}'
print(s.format(35 * 35))

# You can sub-class strings in Python
class MyString(str): # put original string class 'str'
    def __str__(self):
        return self[::-1] # print in reverese
s = MyString('YnneL')
print(s)