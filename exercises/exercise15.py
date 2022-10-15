######################################
# file: exercise15
# Source: Learning Python the Hard Way by Zed Shaw
# Date: 10/14/22
# Purpose: Reading files.
######################################

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's yoru file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

text_again = open(file_again)

print(text_again.read())

