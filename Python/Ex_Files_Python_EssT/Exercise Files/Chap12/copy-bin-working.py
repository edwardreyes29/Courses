#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('berlin.jpg', 'rb') # Can't open with text, this reads a binary file
    outfile = open('berlin-copy.jpg', 'wb') # write mode and binary mode
    while True: # will run continously until reach a break
        buf = infile.read(10240) # 10k bytes -> for mobile envirionments where memory is small (Takes in 10k bytes at a time)
        if buf: # test if there is there is data in the buffer, if an empty buffer or None will have a false comparative value
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()

# Binary file is a file sotred in binary format. A binary file is computer-readable but not human-readable
# All executanble programs are stored in binary files
# This program succesfully copies a binary file

# buf = infile.read(10240) -> don't want to read entire file at once, don't know how much memory is available for your program
# -> so pick a buffer size that you know will be safe
# read(size=-1) -> Read up to size bytes from the object and return them. 
# When copying a binary file, always consider buffer size