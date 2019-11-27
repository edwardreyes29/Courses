#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('lines.txt', 'rt') # opening in read mode 'r' and text mode 't' -> this is default
    outfile = open('lines-copy.txt', 'wt') # this file doesn't exist yet, will be created in write mode and in text mode 
    for line in infile:
        print(line.rstrip(), file=outfile) # use print to write the file
        print('.', end='', flush=True)
    outfile.close() # data may not be all written by the time the main function end, so do this to prevent any data loss
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()

# rstrip() used to rmove line endinges from the file. 
# print('.', end='',flush=True) -> end='' prevents a new line after each dot, flush -> flushes output buffer -> on some OS, outputer buffer is flushed
# with print function, able to strip line endings
# if file is from a different operating system with different line endings,
# - this serves to translate those line endings into the correct one for this
# - operating system