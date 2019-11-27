#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # kitten('meow', 'grrr', 'purr')
    x = ('meow', 'grrr', 'purr', 'roarrr')
    print(*x) # passes reference to the same object
    # print(x) # prints out the tuple itself

# traditional to name this *args -> which is actually a tuple
def kitten(*args): # Allows you to pass a variable number of arguments to a function
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
