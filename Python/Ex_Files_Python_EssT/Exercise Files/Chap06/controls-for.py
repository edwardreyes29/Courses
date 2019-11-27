#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' ) # tuple

for pet in animals:
    if pet == 'dog': continue
    if pet == 'velociraptor': continue
    # if pet == 'bunny': break
    print(pet)
else:
    print('that is all of the animals')