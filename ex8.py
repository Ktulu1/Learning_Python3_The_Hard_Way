# defining a variable that is made up of 
formatter = "{} {} {} {}"

# use format to pass numbers into the {}'s in the formatter variable 
print(formatter.format(1, 2, 3, 4))
# use format to pass text strings into the {}'s in the formatter variable 
print(formatter.format("One", "two", "three", "four"))
# use format to pass boolean operators into the {}'s in the formatter variable 
print(formatter.format(True, False, False, True))
# use format to pass the formatter variable into the {}'s in the formatter variable resulting in 16 {}'s
print(formatter.format(formatter, formatter, formatter, formatter))
# use format to pass text strings into the {}'s in the formatter variable but structure the print command over serveral lines instead of one 
print(formatter.format(
    "Try your", 
    "Own text here", 
    "Maybe a poem", 
    "Or a song about fear"
    ))