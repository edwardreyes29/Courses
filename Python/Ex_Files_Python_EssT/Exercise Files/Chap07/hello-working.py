#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def f1():
#     print('this is f1')

# x = f1
# x() # can call f1 function by now using x, since x is also a function

# def f1():
#     def f2():
#         print('this is f2') # [2]
#     return f2

# x = f1()
# x() # call x like it's a funciton (it is)

# [2] Cannot call f2 directly
# also, can define a function within a function, wild..
# f1 runs the function f2, sinc the return value is the object f2

def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2

@f1 # decorator [3]
def f3():
    print('this is f3')

# x = f1(f3)
# x()

# f3 = f1(f3)
f3() # f3 is no longer directly available, it serves same functionality as x
     # becomes a wrapper itself

# [3] it takes f3 function and it passes it as an arguement to teh decorator function
# and it returns and assignes the name of f3 to the wrapper itself. Can no longer call
# d3 directly, only call it throught the wrapper and f3 now is wrapped inside decorator
# function



