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

#echo the following to the screen
print("Type the filename again:")
#take input 
file_again = input("> ")

#open the file input as variable file_again
txt_again = open(file_again)

#echo the contents of the file to the screen using variable.read
print(txt_again.read())
