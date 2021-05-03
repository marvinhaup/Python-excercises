# Code for Checking if a specific file exists in the filesystem
import os.path

# Define a filename.
filename = "Gästeliste.txt"

if not os.path.isfile(filename):
    print("File does not exist.")
else: 
# Open the file as f.
# The function readlines reads the file.
# The function splitlines() disregards the newline character
    with open(filename) as f:
        content = f.read().splitlines()

# Show the file contents line by line.
# We added the comma to print single newliness and not double newlines.
#This is because the lines contain the newline character '\n'
for line in content:
    print(line)