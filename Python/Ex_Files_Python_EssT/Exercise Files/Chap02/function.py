#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n):
    print(n)

function(47)


def helloThere():
    print('General Kenobi')

helloThere()

# Functions defined wiht 'def'
# some take arguments and some do not.

def add(a, b):
    print(a + b)

add(5, 6)

# Can provide functions with default values!
def function2(n = 1):
    print(n)

function2() # if function has default value, no need for arg
function2(5)

def getValue():
    return 818

print(getValue())