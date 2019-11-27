def isprime(n):
    if n < 1:
        return False
    for x in range(2, n): # [2, 3, 4] check every number until it reaches itself
        if n % x == 0:
            return False
    else:
        return True

n = 9
if isprime(n):
    print(f'{n} is prime')
else:
    print('{} not prime'.format(n))

print(list(range(2,5))) # range(start, stop)
print(list(range(1,11)))
print(list(range(5)))

# Give list of primes
def list_primes():
    for n in range(100):
       if isprime(n):
           print(n, end=' ', flush=True) # ends print with space, other flushe output buffer
    print()

list_primes()