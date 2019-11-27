#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)

    # dictionary constructor
    print()
    sigils = dict(dragon = 'fire and blood', wolf = 'winter is coming', lion = 'hear me roar')
    print_dict(sigils)

    # items method
    print()
    print('Items method')
    for k, v in animals.items():
        print(f'{k} : {v}')
    # print(animals.items())

    # keys method 
    print()
    print('<<<Keys>>>')
    for k in animals.keys():
        print(f'{k}')
    
    # values method
    print()
    print('<<<values>>>')
    for v in animals.values():
        print(f'{v}')\

    # Dictionaries are indexed by their keys
    print()
    print('season 1: ')
    print(sigils['wolf'])

    # Assign different value to wolf 
    print('season 8: ')
    sigils['wolf'] = 'Ah dun wan et'
    print(sigils['wolf'])

    # Add new item
    print()
    sigils['squid'] = 'we do not sow'
    print_dict(sigils)

    # Check if item is in dictionary
    print('lion' in sigils) # True
    print('fish' in sigils) # False

    if 'wolf' in sigils:
        print('DAKINGINDANORF!')
    else:
        print('nope')

    # Get method -> returns a value if you don't know if it exists
    # Use if you don't want the exception 
    print(sigils.get('lion')) # returns value
    print(sigils.get('godzilla')) # returns None

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()
