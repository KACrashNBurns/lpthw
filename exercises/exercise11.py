######################################
# file: exercise11
# Source: Learning Python the Hard Way by Zed Shaw
# Date: 10/14/22
# Purpose: getting input from the user
######################################

print("How old are you? ", end='') # end='' tells the print not to tnd the line with a newline characet or go to the next line.
age = input()
print("How tall are you? ", end='')
height = input()
print("How much do you weigh? ", end='')
weight = input()

print(f"So, you're {age} old, {height} tall, and {weight} heavy.")