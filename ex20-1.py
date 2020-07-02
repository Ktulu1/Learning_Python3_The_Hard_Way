# import argv from library sys
from sys import argv

# setup variables for argv
script, input_file = argv

# define a function that prints the entire contents of the file
def print_all(f):
    print(f.read())

# define a function that seeks to the begining of the file
def rewind(f):
    f.seek(0)

# define a fuction that prints a specific line in the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# set the a variable for the open file
current_file = open(input_file)

# echo this text to the screen
print("First let's print the whole file:\n")

# call the function print_all
print_all(current_file)

# echo this text to the screen
print("Now let's rewind, kind of like a tape.")

# call the function rewind
rewind(current_file)

# echo this text to the screen
print("Let's print three lines:\n")

# set a variable for line number
current_line = 1
print(f"Current line is {current_line}")
# call the function print_a_line and pass the line number and file object variables
print_a_line(current_line, current_file)

# take the variable for line number and increment it by 1
current_line += current_line
print(f"current line is {current_line}")
# call the function print_a_line and pass the line number and file object variables
print_a_line(current_line, current_file)

# take the variable for line number and increment it by 1
current_line = current_line + 1
print(f"Current line is {current_line}")
# call the function print_a_line and pass the line number and file object variables
print_a_line(current_line, current_file)