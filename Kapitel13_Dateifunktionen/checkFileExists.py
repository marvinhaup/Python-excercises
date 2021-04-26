# programming structure to check if a specific file exists or not

# Version 1 and 2 both work without importing any external libraries
# Version 1 and 2 also also the preferred version when neeeding to open and write to them

# version 1

try:
    fid = open("filename.txt")
    # Do something with the file
except IOError:
    print("File not accessible")
finally:
    fid.close

# version 2 (No need to close the file after usage)

try:
    with open('filename.txt') as fid:
        print(f.readlines())
        # Do something with file
except IOError:
    print("File not accessible")


# Checking if file exits with os.path module

# os.path.exists(path) Returns True if path is a File or Directory
# os.path.isfile(path) Returns True if path is a File
# os.path.isdir(path) Return True if path is a Directory

# Better for file-operations like copying ir deleting

import os.path

if os.path.isfile('filename.txt'):
    print("File exists")
else:
    print(("File doesn't exist"))


# Checking if file exists using the pathlib module
# pathlib provides the ability to work with files as objects, such as methods or attributes
# whereas os.path only provides string operations with files

from pathlib import Path

if Path('filename.txt').is_file():
    print("file exists")
else:
    print("File doesn't exist")