#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('Meow.')
    # return 42 # returns an Int
    # return [42, 43, 44] # returns a list
    return dict(x = 1, y = 2, z = 3) # returns a dictionary
if __name__ == '__main__': main()

#[Notes]   
# - If no return statement, function returns none