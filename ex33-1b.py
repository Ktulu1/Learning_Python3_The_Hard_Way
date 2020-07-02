#i = range(0, 6)
numbers = []


for i in range(0, 6):
    print(f"at the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"at the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print (num)
