#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'the number of bunnies is {self._n} 👐'
    def __str__(self):
        return f'str: the number of bunnies is {self._n}'
        
s = 'Hello, World.'
#repr will print the string itself
print(repr(s))

x = bunny(47)
print(repr(x)) # returns the memory address of this bunny object
print(x) # returns similar output. Will take the string method instead of __repr__

# ASCII function
print()
print(ascii(x)) # use repr method, will escape special characterss
print("\U0001f450")
print("\U0001f602")
# chr function
print()
print(chr(128406)) # prints the character represented by the Unicodes position
print(chr(128080))
# ord function
print()
print(ord('👐')) # return number of a chacter, chr, returns a character of a number
