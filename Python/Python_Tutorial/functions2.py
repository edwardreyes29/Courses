# Default argument values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# can be called in several ways:
ask_ok('Do you really want to quit? ')
ask_ok('OK to overwrite the file? ', 2) # set retries to 2
ask_ok('Ok to overwrite the file? ', 2, 'Come on, only yes or no!') # set new reminder

# in keyword: tests whether or not a sequence contains a certain value

i = 5
def f(arg=i):
    print(arg)

i = 6
f()

# Default value is evaluated only once. Makes a difference when deault is mutable
# such as a list, dictionary, or instance of most classes.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(3))
print(f(5))

# if you don't want default to be shared:
def f(a, L=None):
    if L is None:
        L = []
    print(L)
    L.append(a)
    return L

print(f(1))
print(f(3))
print(f(5))