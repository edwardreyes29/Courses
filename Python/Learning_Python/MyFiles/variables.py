f = 0
# print(f)
# f = "abc"
# print("this is a string " + f) # causes error
# print("this is a string " + str(123))

# Global vs. local variables in functions
def someFunction():
    global f # target global variable
    f = "def" # local variable
    print(f)

someFunction()
print(f)

del f # deletes definition of a variable that was previously declared
print(f) # global name 'f' not defined