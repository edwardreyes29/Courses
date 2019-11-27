#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    # No longer setting default values
    # This is will be the base class and it's going to be inheritd in order to be used
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t = None):
        if t: self._type = t
        try: return self._type # Need to check if there is data
        except AttributeError: return None

    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None

# Created other classes that inherit from Animal
class Duck(Animal): # Inheriting from Animal
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type'] # if there is a type in kwarg then delete that
        super().__init__(**kwargs) ## Call parent class initializer with our kwargs
        # Super always calls parent class

class Kitten(Animal): # Inheriting from Animal
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        # print(kwargs) # {'name': 'fluffy', 'sound' : 'rwar'}
        super().__init__(**kwargs)
    # Special case for this class
    def kill(self, s,): # let s represent prey
            print(f'{self.name()} will now kill all {s}!')

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')

def main():
    a0 = Kitten(name = 'fluffy', sound = 'rwar')
    a1 = Duck(name = 'donald', sound = 'quack')
    print_animal(a0)
    print_animal(a1)

    a0.kill('humans')

    # type Tiger gets deleted, so you can't set type of a class
    a3 = Kitten(type = 'Tiger', name = 'Tony', sound = 'Theerrrrrrrre GRRRRREATTT!', cash = "$1100")
    print_animal(a3)

if __name__ == '__main__': main()


# self will reference the object, not the class itself
# [def __init__] acts as a constructor