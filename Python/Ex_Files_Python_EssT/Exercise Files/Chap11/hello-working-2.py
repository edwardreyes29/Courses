#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')
print('Hello, World'.upper())
print('Hello, World'.lower())
print('hello, world'.capitalize()) # Capitalizes just the first letter
print('hello, world'.title()) # capitalizes first letter of every word
print('Hello, World'.swapcase()) # swap cases of letters

print('Hello, World. ß'.casefold()) # more aggressive version of lower(), removes case disticntion even in unicode
print('Hello, World. Straße'.casefold())

# Remember, strings are immutable.
s1 = 'Hello, world'
s2 = s1.upper()

print(id(s1))
print(id(s2))

# concatenate
print(s1 + ' ' + s2)
s3 = 'this string' ' that string'
print(s3)

# https://docs.python.org/3/library/stdtypes.html