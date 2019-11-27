#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('/Users/edwardreyes/desktop/lines.txt') # creates a text stream (iterator: countale number of values)
    print(f)
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()

# open function returns a file object
# The file object itself is an iterator - can use a for loop to get one line at a time with having to buffer the entire file in memory
# rstrip(): Retrun copy of string with trailing characters removed. - Defaults to whitespace
print('     spacious        '.rstrip())
print('mississippi'.rstrip('ipz'))
print('spacious'.rstrip('ous'))