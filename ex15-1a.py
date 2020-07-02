#includes argv from sys library
from sys import argv

#define the variables for argv
script, filename = argv

#open the file named in argv
txt = open(filename)

#echo the variable "filename" to the screen
print(f"Here's your file {filename}:")
#echo the contents of the file to the screen using variable.read
print(txt.read())

txt.close()