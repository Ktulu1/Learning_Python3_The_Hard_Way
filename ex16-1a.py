from sys import argv

script, filename = argv

txt = open(filename)

print(f"\nOpening {filename}... \n")
print(txt.read())

txt.close()

