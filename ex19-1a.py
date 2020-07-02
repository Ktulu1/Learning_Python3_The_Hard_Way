from sys import argv
script, read_argv, owned_argv = argv

def books(books_read, books_owned):
    books_to_go = (books_owned - books_read) 
    print(f"\tYou have read {books_read} books of the {books_owned} you own. You have {books_to_go} left to read.\n")

print("1. Passing numbers to a function:")
books(500, 1500)

print("2. Passing variables to a function:")
read = 20
owned = 50
books(read, owned)

print("3. Passing variables for a function from argv:")
books(int(read_argv), int(owned_argv))

print("4. Passing math to a function (10+5 and 20+5):")
books(10 + 5, 20 + 5)

print("5. Passing variable from input to a function:")
prompt = "> "
print("\tHow many books do you own?")
owned_input = input(prompt)
print("\tHow many have you read?")
read_input = input(prompt)
books(int(read_input), int(owned_input))

print("6. Passing variables with math to a fuction:")
books(read + 5, owned + 5)

print("7. Adding variables together and passing them to a fuction:")
books(int(read) + int(read_argv), int(owned) + int(owned_argv))

print("8. Adding variables together and number and passing them to a function:")
books(int(read) + int(read_argv) + 5, int(owned) + int(owned_argv) + 5)

print("9. Passing input with math to a function:")
books(int(read_input) + 5, int(owned_input) + 5)

print("10. Passing input from argv with math to a function:")
books(int(read_argv) + 5, int(owned_argv) + 5)