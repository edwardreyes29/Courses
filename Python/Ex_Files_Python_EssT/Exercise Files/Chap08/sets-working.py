#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)

    a = set("12345")
    b = set("1356789")

    # sort them
    print()
    print('<<<Sorted>>>')
    print_set(sorted(a))
    print_set(sorted(b))

    # - operator 
    # all members in a and not b
    print()
    print('<<< - operator >>>')
    print_set(a - b)

    # | operator
    # all of the members in one or both of the sets
    print()
    print('<<< | operator >>>')
    print_set(a | b)

    # ^ operator (caret)
    # all elements in a or b but not both
    print()
    print('<<< ^ operator >>>')
    print_set(a ^ b)

    # & operator
    # only member in both
    print()
    print('<<< & operator >>>')
    print_set(a & b)

    
def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
