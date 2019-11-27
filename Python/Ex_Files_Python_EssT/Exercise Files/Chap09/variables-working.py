#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    # Not encapsulated
    x = [1, 2, 3] # class variable. defined in class and not in any method

    def __init__(self, **kwargs):
        # all three are encapsulated
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        # Using the getters to access variables, SAFE!!!
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)

    # a0._name = 'Joe'    # Don't do this in practice
    # print(a1._name)     # to demonstrate that these varaibles belong to the object

    print(a0.x) 
    a1.x[0] = 7 # change class variable 
    print(a0.x) # the change affects all objects with the same class
                # Object doesn't have this variable, it's draeing it from the class 

if __name__ == '__main__': main()
