from sys import argv

script, filename = argv

target = open(filename, 'w')

target.close()
