#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' ) # tuple!
y = 'bear'

# if a and b:
#     print('expression is true')
# else:
#     print('expression is false')    

# if a or b:
#     print('expression is true')
# else:
#     print('expression is false')

# if not a:
#     print('expression is true')
# else:
#     print('expression is false')

# if not b:
#     print('expression is true')
# else:
#     print('expression is false')

if y in x: # since x is a collection
    print('expression is true')
else:
    print('expression is false')

if 'leaf' in x: # since x is a collection
    print('expression is true')
else:
    print('expression is false')

if 'tree' in x: # since x is a collection
    print('expression is true')
else:
    print('expression is false')

if y is x[0]: # strings are not mutable. 
    print('expression is true')
else: 
    print('expression is false')

print(id(y))
print(id(x[0]))

if y is not x[0]: 
    print('expression is true')
else: 
    print('expression is false')

if y is not x[1]: 
    print('expression is true')
else: 
    print('expression is false')