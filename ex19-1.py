# defines the function "cheese_and_crackers" which echos some stuff to the screen
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

# calls and passes numbers to a function
print("We can just give the fuction numbers directly:")
cheese_and_crackers(20, 30)

# calls and passes variables to a function - which seems to be the same as passing numbers. Might be converting the variable to a number and passing just the numbers. Don't know.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calls and passes math to a function - which seems to be the same as passing numbers. Might be doing math first and then just passing numbers. Don't know.
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# calls and passes variables that have math performed on them to function
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)