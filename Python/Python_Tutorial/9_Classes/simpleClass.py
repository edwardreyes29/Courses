class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# MyClass.i and MyClass.f are valid references.
print(MyClass.i)
print(MyClass.f()) # errior
# __doc__ is a valid attribute
print(MyClass.__doc__)

x = MyClass()   # function notation
print(x.i)
print(x.f) # method reference, since MyClass.f is a function. x.f() is method object, MyClass.f() is function object
print(x.f()) # x.f() == MyClass.f(x)

# Data attributes do not need to be declared. 
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter  

# can store method object
xf = x.f
# while True:
#     print(xf())