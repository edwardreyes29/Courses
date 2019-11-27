#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# List created with square brackets
x = [ 1, 2, 3, 4, 5 ]

# List's are mutable, can reassign values after assigning them
x[2] = 42
x[0] = 36
# The for loop is sequencing throught the list
# for each item in the list, it assigns 'i' the value of the item
for i in x: 
    print('i is {}'.format(i))

print()

# Tuple is created with parentheses
x = ( 6, 7, 8, 9, 10 )
# x[4] = 5 -> will not work, tuple is not mutable -> immutable
for i in x:
    print('i is {}'.format(i))
    
print()

# create a sequence using range
x = range(10) # 0 to 9
for i in x:
    print(f'i is {i}')

print()

x = range(5, 10) # 5 to 
for i in x:
    print(f'i is {i}')

print()

x = range(5, 20, 2) # 5 to 20, stepping by 2
for i in x:
    print(f'i is {i}')

print()

# can create a mutable list using range
# Construct a list with the result of range
y = list(range(4, 12, 3))
for i in y:
    print('i is {}'.format(i))
print()
y[1] = 55
for i in y:
    print('i is {}'.format(i))

print()

# Dictionaries
x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
x['three'] = 300

# prints out the keys
for i in x:
    print('x is {}'.format(i))

print()

# to print out keys & values in dictionaries
for k, v in x.items(): # returns a 2-tuple of each items with key & value
    print('k: {}, v: {}'.format(k, v))

