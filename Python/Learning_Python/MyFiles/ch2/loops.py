def main():
    x = 0

    # Python only has two ways of doing loops: while & for

    # while(x<5):
    #     print(x)
    #     x = x+1

    # different than traditional for loops: for (i=0; x < 10; i++)
    # for loops are iterators.

    # for x in range(5, 10): # 10 not inclusive in the range
    #     print(x)

    # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] # list
    # for d in days:
    #     print(d)

    # for x in range(0,10):
    #     if (x==7): break # breaks execution of loop if condition is met (inner most)
    #     print(x)

    # for x in range(0,10):
    #     if (x % 2 == 0): continue # skips current iteration
    #     print(x)

    # enumerate() function
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
    for i,d in enumerate(days): # returns index and value
        print(i, d)

if __name__ == "__main__":
    main()