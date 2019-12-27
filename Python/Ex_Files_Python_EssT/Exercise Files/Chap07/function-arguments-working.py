#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = [5] # x will be a call by value, so value is passed and not the object itself for O-O
            # but in python, integers are immutable, so it simply creates a new integer variable
            # it all cases, its call by reference, and when variable is immutable, its creates a new object
    y = x
    # y = 3 # will have different id number
    y[0] = 3 # list are mutable, so changes value in both x and y since the same object is being changed
    print(id(x))
    print(id(y))
    print(x)
    print(y)
    kitten(x, 6)
    print(f'in  main: x i s {x}')


# any arguments with default values must be after ones without default values
# (!) Rule of thumb: if args have default values, make all of them have default values
def kitten(a, b, c = 0):
    print(id(a)) # same id as x
    a[0] = 8
    print(id(a)) # different id as x
    print('Meow.')
    print(a, b, c)

if __name__ == '__main__': main()
