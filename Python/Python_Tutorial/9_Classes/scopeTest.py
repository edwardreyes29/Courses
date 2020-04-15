def scope_test():
    def do_local(): # doesn't change scope_test's binding of spam.
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam   # changes scope_test's binding of spam
        spam = "nonlocal spam"

    def do_global():
        global spam     # changes module-level binding
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)