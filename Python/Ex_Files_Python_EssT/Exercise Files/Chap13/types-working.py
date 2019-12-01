#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47' # literal string
y = int(x) # (Int function) actually the constructor for int type


print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

print()
y = float(x)
print(f'y is {type(y)}')
print(f'y is {y}')

print()
x = -47
y = abs(x) # returns absolute value of x
print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')


# divmod
print()
x = 47
y = divmod(x, 3) # returns quotient and remainder in a tuple of division
# 47 / 3 returhsn 15, with remainder of 2
print(f'y is {type(y)}')
print(f'y is {y}')

# complex -> type constructor
# complext numbers are two dimensional numbers, using j instead of i for imaginary part
print()
y = x + 73j
print(f'y is {type(y)}')
print(f'y is {y}')