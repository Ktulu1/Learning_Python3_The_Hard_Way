from sys import argv


script, name = argv

print("Script:", script)
print(f"What is you last name {name}?")
last_name = input()
print(f"Welcome {name} {last_name}!")

