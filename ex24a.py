def secret_formula(starting):
    more = starting * 2
    less = more - 1
    win = less * more
    return more, less, win

start_point = 10
jump, shit, die = secret_formula(start_point)

print(f"More = {jump} \nLess = {shit} \nWin = {die}")