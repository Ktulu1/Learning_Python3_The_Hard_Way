
numbers = []

def nums(start, stop, step):
    while start < stop:
        print(f"At the top start is {start}")
        numbers.append(start)

        start += step
        print("Numbers are now: ", numbers)
        print(f"At the bottom start is {start}")


#print("The numbers: ")
start_point = 2
stop_point = 60
step_point = 10
nums(start_point, stop_point, step_point)

#print(num)