#
# Example file for working with conditional statements
#

def main():
    x, y = 100, 100

    if (x < y):
        st = "x is less than y"
    elif (x > y):
        st = "x is greater than y"
    else:
        st = "x is equal to y"

    print(st)

if __name__ == "__main__":
    main()


# max=x if (x>y) else y
# same as:
# max=y
# if (x>y):
#   max=x