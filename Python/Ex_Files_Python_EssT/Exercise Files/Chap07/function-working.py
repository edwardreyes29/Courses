#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = [5]
    kitten(x)
    print(f'in main: x is {x}')
    # x = [5] # make x a list, which is mutable
    # y = x
    # y[0] = 3
    # print(id(x)) # x & y have the same id
    # print(id(y))
    # print(x)
    # print(y)

# def kitten(n):
#     print(f'{n} Meow.')

# def kitten():
#     # print('Meow.') # Returns None, all functions return a vlaue
#     # return 'Meow' # Returns a literal String

# def kitten(a, b, c):
#     print('Meow')
#     print(a, b, c)

# def kitten(a, b, c = 0): # Give argument 'c' a default value
#     print('Meow.')
#     print(a, b, c)

def kitten(a):
    a[0] = 3 # will change x in main, this is strictly call by reference
    print('Meow.')
    print(a)

if __name__ == '__main__': main() # very commonly used

# >>> if __name__ == '__main__': main()
# if statement calls main, which calls kitten, but kitten is already defined 
# at this point. You won't be able to call kitten before.

# special varaible __name__ will return the name of the current module
# In this case, main is defined after this. So its okay, you can call a function
# if it has been called beforehand. But in main, it calls kitten, which has been
# defined after. So if we didn't have this statement above and we didn't have a
# function main but we had a function defined after it, we would not be able
# to call it.
# This is the standard work around for no support of 'for declarations'


