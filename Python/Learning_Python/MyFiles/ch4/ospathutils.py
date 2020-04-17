import os
from os import path
import datetime
from datetime import date, time, timedelta, datetime
import time 

def main():
    # print name of the OS
    print(os.name)  # posix
    
    # Check for item existence and type
    # print("Path: " + str(path.dirname("textfile.txt")))
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a file: " + str(path.isfile("textfile.txt")))        # True
    print("Item is a directory: " + str(path.isdir("textfile.txt")))    # False

    # Work with file paths
    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))
    print("Dirname: " + str(path.dirname(path.realpath("textfile.txt"))))


    # Get file modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the item was modified
    td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since the file was modified.")
    print("Or " + str(td.total_seconds()) + " seconds.")

    # Calculate how long ago the item was modified for backup
    print("Backup: ")
    td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt.bak"))
    print("It has been " + str(td) + " since the file was modified.")
    print("Or " + str(td.total_seconds()) + " seconds.")
if __name__ == "__main__":
    main()