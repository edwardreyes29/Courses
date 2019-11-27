# use recursion to implement a countdown counter



def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1) # once x == 0 is true, the return statement will return to this statement of the previous call and back until it exits function
        print("foo") # once this print, then funciton will exit, and will keep on happening untill we reach top of call stadk

countdown(5)
