#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    count = 1 # I forgot, this is not mutable!!!!
    x = [1, 2, 3] # does encapsulation only work for list???s
    count2 = [0]
    # def __init__(self, type, name, sound): # pass three arguments, the first is always 'self'
    #     # Object variables
    #     self._type = type # _ underscores are traditional, discourages users of object from accessing these directly
    #     self._name = name
    #     self._sound = sound

    # Alternative, using keyword generator & give default values
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'
    

    # Getters -> Accesors
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    # a0 = Animal('kitten', 'fluffy', 'rwar')
    # a1 = Animal('duck', 'donald', 'quack')
    
    # using **kwargs
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a0.count2[0] += 1
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    a1.count2[0] += 1
    print(a0.count2[0])
    print_animal(a0)
    print_animal(a1)
    
    # calls class without creating an intermediary object
    # print_animal(Animal('velociraptor', 'veronica', 'hello')) 

    # using **kwargs
    print_animal(Animal(type = 'velociraptor', name = 'veronica', sound = 'hello'))

    # Test default values
    print_animal(Animal()) # can just call Animal class with nor data
    print_animal(Animal(species = 'monkey', nickname = 'Kongo', noise = 'eeee eeee'))

    # a1.count = 4
    # print(a0.count)
    # print(a1.count)
    # print(a0.x)
    # a1.x[0] = 8
    # print(a0.x)
if __name__ == '__main__': main()
