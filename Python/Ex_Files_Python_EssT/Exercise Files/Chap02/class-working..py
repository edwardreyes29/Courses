#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck: # : introduces contents of function or class
    # The first argument for a method inside of a class is
    #  always self (not a keyword but recommended) 
    # it's a reference to the object when the class is used to 
    # create an object

    sound = 'Quack'
    walking = 'Walks like a duck.'
    def quack(self): # function
        print(self.sound)

    def walk(self): # function
        print(self.walking)

class Dog:
    def bark(self):
        print('Woof woof')

    def walk(self):
        print('Going for a walk.')

def main():
    donald = Duck() # Assign donald from the class, now donald is an object
    donald.quack()  
    donald.walk()

    americanCattleDog = Dog()
    americanCattleDog.bark()
    americanCattleDog.walk()

if __name__ == '__main__': main()


