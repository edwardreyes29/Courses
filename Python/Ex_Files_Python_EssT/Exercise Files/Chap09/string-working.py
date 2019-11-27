#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class RevStr(str): # inheriting from str
    def __str__(self): # Overriding the string representation method
        return self[::-1] # return slice of the string where the step goes backwards, reversing string

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()
