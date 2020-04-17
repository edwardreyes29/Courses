def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    # f = open("textfile.txt", "a")

    # Read contents of a file
    f = open("textfile.txt", "r")


    # for i in range(10,20):
    #     f.write("This is line " + str(i) + "\r\n")

    if f.mode == 'r':
        # contents = f.read()
        # print(contents)

        # read line by line
        fl = f.readlines()
        for x in fl:
            print(x)

    f.close()


if __name__ == "__main__":
    main()