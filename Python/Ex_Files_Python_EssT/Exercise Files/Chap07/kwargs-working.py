#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr') # Syntax for dictionary
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)
def kitten(**kwargs): # dictionaries instead of tuples, follow this convention
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()
