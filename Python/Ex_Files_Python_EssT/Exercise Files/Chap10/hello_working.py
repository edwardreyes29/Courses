#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys

def main():
    # ValueError error itself, token, the name of a type of error being genrated
    # Catch the error with try command
    # Prevents execution form terminating, so execution will still continue if you run into this error
    try:
        x = int('foo')
    except ValueError: # if try fails, this will be executed
        print('I caught a ValueError')
    
    # x = 5/0
    try:
        # x = 5/0
        x = int('foo')
    except ZeroDivisionError:
        print('I caught a ZeroDivisionError')
    except:
        # use sys to know more about error, impot sys/ use [1] supscript to get the specific error
        print(f'unknown error: {sys.exc_info()[1]}') # Use this if error is not known
    else: # executes if no error
        print('good job!')
        print(x)


if __name__ == '__main__': main()
