#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    # Data
    sound = 'Quack quack.' 
    movement = 'Walks like a duck.'

    # Methods
    def quack(self): # [1], self is a reference to the object, not the class
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack() # Invoke object method quack, [2]
    print(donald.sound) # can print the data itself, not recommended
    donald.move()

if __name__ == '__main__': main()

# [1]
# 'self' is not a keyword, but it's a naming convention that should be used
# self is a reference to the object, not the class. When object is created 
# from the class, 'self' will reference the object, not the class

# [2]
# dot (.) operator dereferences the object so that you can get to the method, in 
# this case quack

# Definition: 
#   dereference: To go to an address before performing the operation