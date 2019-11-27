#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s)

# split method splits string into a list, where each word becomes an element of this list
print(s.split())
print(s.split('i'))
print(s.split('st',-1))
print('1,,2'.split(',,'))
print('1<>2<>3'.split('<>'))

l = s.split()
s2 = '--'.join(l) # the string is the separater that the string will be joined with
print(s2)
s3 = '?'.join(s)
print(s3)