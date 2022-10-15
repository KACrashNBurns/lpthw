######################################
# file: exercise5
# Source: Learning Python the Hard Way by Zed Shaw
# Date: 10/14/22
# Purpose: Demonstrate More Variables and Printing
######################################

my_name = "Frank E. Ciszek"
my_age = 41 # not a lie
my_height = 69 #inches
my_eyes = 'Grey'
my_teeth = 'White'
my_hair = 'Grey'

print(f"Lets talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"He's a handsome fella.") # Not really
print(f"His teeth are usually {my_teeth} depending on the coffee")

# This line is tricky, get it exactly right.

total = my_age + my_height
print(f"If I add {my_age} and {my_height} I get {total}.")