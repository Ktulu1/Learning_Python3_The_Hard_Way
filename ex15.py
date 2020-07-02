# import argv from the sys library
from sys import argv

# define variables for argv
script, filename = argv

# define the variable "txt" as the open file
txt = open(filename)

# echo the variable "filename" to the screen
print(f"Here's your file {filename}:")
# echo the variable "txt" to the screen using read to read the file
print(txt.read())

# prompt for the filename while in the script using input()
print("Type the filename again:")
file_again = input("> ")

# define the variable "txt_again" as the open file... again
txt_again = open(file_again)

# ech the variable "txt_again" to the screen using read to read the file... again
print(txt_again.read())

txt.close()
txt_again.close()

