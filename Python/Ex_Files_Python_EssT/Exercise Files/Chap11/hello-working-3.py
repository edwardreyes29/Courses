#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73
print('the number is {} {}'.format(x, y))
print('the number is {xx} {bb}'.format(xx = x, bb = y))
print('the number is {xx} {bb}'.format(bb = x, xx = y))
print('the number is {0} {1}'.format(x, y))
print('the number is {1} {0}'.format(x, y))
print('the number is {1} {0} {1} {0}'.format(x, y))

# Can add formatting instructions
print()
print('the number is {0:<5} {1:>5}'.format(x, y))
print('the number is {0:<5} {1:>05}'.format(x, y)) # add leading zeros
print('the number is {0:<5} {1:+}'.format(x, y)) #add a sign
print('the number is {0:<5} {1:+05}'.format(x, y))
print()

x = 42 * 74 * 1000
print('the number is {:,}'.format(x)) # format with commas
print('the number is {:,}'.format(x).replace(',', '.')) # (Euro) replace commas with periods
print()
# Specify decimal places
# f - floating point display
x = 2 / 3
print('**the number is {:f}'.format(x))
print('the number is {:.3f}'.format(x))
print('the number is {:.2f}'.format(x))
print()
# put in hexadecimal
# x - hexadecimal display
x = 42
print('the number is {:x}'.format(x))
# binary
# b - binary display
print('the number is {:b}'.format(x))
print()
# Alternative format method
x = 56
y = 54
print(f'the number is {x} {y}')
print(f'the number is {x:.3f} {y}')

# x = 1
# 'Some random sentence '.format(x)
# f'Some random setence {x}'