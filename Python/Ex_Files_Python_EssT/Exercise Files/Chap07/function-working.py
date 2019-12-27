#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     kitten()
#
# def kitten():
#     print('Meow.')

# def main():
#     kitten(5, 4, 3, 2, 1)
#
# def kitten(a, b, c, d, e):
#     print(f'{a}, {b}, {c}, {d}, {e}, Meow.')

# all functions return a value
def main():
    x = kitten()
    print(x)
def kitten():
    print('Meow.') # Doesn't explicitly return a value, by default returns None
    return 'Meow.' # here we explictily return a value

if __name__ == '__main__': main()
# if this file was imported by another module, main will be the name of the this module.

