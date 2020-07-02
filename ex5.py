name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teath = 'White'
hair = 'Brown'
metric_length = 2.54 # centimeters per inch
metric_mass = .4536 # kilograms per pound
height_metric = height * metric_length
weight_metric = weight * metric_mass

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teath are usually {teath} depending on the coffee.")

# this line is tricky, try to get it exacty right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"Zed's height in centimeters is {height_metric} and his weight is {weight_metric}.")

