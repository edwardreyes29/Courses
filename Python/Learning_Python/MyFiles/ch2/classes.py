# Classes, encapsulate functionality that can be used as a complete module for other projects

class myClass():
    def method1(self): # first arg is the self argument. self argument refers the object itself
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)

# inheritance
class anotherClass(myClass):
    def method1(self): # first arg is the self argument. self argument refers the object itself
        myClass.method1(self) # call method1 from super class
        print("anotherClass method1")

    def method2(self, someString): # overrides method from base class
        print("anotherClass method2 ")

class Person():
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSex(self):
        return self.__sex

def main():
    c = myClass() # instantiates object instance of this class
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")

    myself = Person("Edward", "29", "Male")
    print(myself.getName())
    print(myself.getAge())
    print(myself.getSex())

if __name__ == "__main__":
    main()

