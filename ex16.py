# load argv from the sys library
from sys import argv

# define variables for argv
script, filename = argv

# echo some text with a varaible in it
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

# set the prompt
input("?")

# echo some text about what's going on
print("Opening the file...")
# open the file as file object "target" in write mode
target = open(filename, 'w')

# more echoed text
print("Truncating the file. Goodbye!")
# use the truncate command on the file object "target"
target.truncate()

# echo some instructions
print("Now we're goign to ask you for three lines.")

# input 3 strings named line1...
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# more status updates echoed to the screen
print("I'm going to write these to the file.")

# use the write command to write the imput from above to the file object "target" and write a new line - 3 times
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# more status echoed
print("And finally, we close it.")
# close the file object "target"
target.close()