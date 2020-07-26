'''
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.

'''
# create/write file
f = open("demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())


# Create a New File
### To create a new file in Python, use the open() method, with one of the following parameters:

### "x" - Create - will create a file, returns an error if the file exist

### "a" - Append - will create a file if the specified file does not exist

### "w" - Write - will create a file if the specified file does not exist

# f = open("myfile.txt", "x")

# Create a new file if it does not exist:

# f = open("myfile.txt", "w")

# deleating a file

# import os
# os.remove("demofile2.txt")


import os
if os.path.exists("G:\\tutorial\python2\demofile.txt"):
  os.remove("G:\\tutorial\python2\demofile.txt")
else:
  print("The file does not exist")

# # deleating a folder
# import os
# os.rmdir("myfolder") #you can only remove empty folder.