def fib(n): # write Fibonacci series up to n
    """ Print a Fibonacci series up to n. """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # return Fibonacci series up to n
    """ Return a list containing the Fibonacci series up to n. """
    result = [] # empty list
    a, b = 0, 1
    while a < n:
        result.append(a) # append to list
        a, b = b, a+b
    return result

# Call the function
fib(2000)

# Assign a function
f = fib
fib(100)
fib(0)          # no output
print(fib(0))   # Functions with not return statement return None

f100 = fib2(100)    # call function
print(f100)         # write the result

for f in f100:
    print(f, end = ' ')
print()

