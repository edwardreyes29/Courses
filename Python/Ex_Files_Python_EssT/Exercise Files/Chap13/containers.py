#!/usr/bin/env python3
print('Hello there')

x = ( 1, 2, 3, 4 , 5 )
y = x
z = len(x)
w = list(reversed(x)) # returns reversed list, can use tuple as well
v = sum(x) # returns sum of each element in the tuple
min = min(x)
max = max(x)


print(x)
print(y)
print(z)
print(w)
for i in w: print(f"{i} 🥓")
print(v)
print()
print(min)
print(max)

# any -> returns true if any is true, not zero is true
x2 = ( 0, 0, 0, 0 ,0 )
print(any(x2))
x3 = ( 0, 0, 1, 0, 0 )
print(any(x3))
# all -> returns true if all values are true
print(all(x3)) 
print(all(x))

# zip
y = ( 6, 7, 8, 9, 10 )
z = zip( x, y ) # zip returns an iterator with two values in each item
for a, b in z: print(f'{a} - {b}')

print()
# enumerate => provieds an index for each element
x = ( 'cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(x): print(f'{i}: {v}')