tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm  \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

formatter = "{} {} {} {}"

print(formatter.format("\n\t* Cat Food" "\t$10", "\n\t* Fishies" "\t$12", "\n\t* Catnip" "\t$5", "\n\t* Grass \t$2.50",))

