#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    v = sys.platform
    print(v)

    v = os.name
    print(v)

    # v = os.getenv('PATH')
    v = os.getcwd() # curren working directory
    print(v)

    v = os.urandom(25).hex() # 25 bytes long in hex
    print(v)

    x = random.randint(1, 1000) # random int between 1 and 1000
    print(x)

    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)


    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)


if __name__ == '__main__': main()
