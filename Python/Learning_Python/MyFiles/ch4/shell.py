#
# Working with file system.
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get path to the file in the current directory
        src = path.realpath("textfile.txt")

        # make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # copy over permissions, modification times, and other info
        # shutil.copy(src, dst)

        # copy with modification time and other metadata -> copystat()
        # shutil.copystat(src, dst)

        # rename the original
        # os.rename("textfile.txt", "newfile.txt")

        # put files into a zip files
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir) # will contain archive of all files in this directory

        # more fine-grained control over ZIP files
        # with keyword creates a local scope to simiplify working with objects
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")    # Will only add these two files into the archive
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()