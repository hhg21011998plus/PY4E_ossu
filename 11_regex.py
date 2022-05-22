import re

# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

typing = input("Enter a regex: ")
fhand = open("mbox.txt")
count = 0

for line in fhand:
    if re.search("%s" %typing, line):
        count += 1

print("mbox.txt had %d lines that matched %s" %(count, typing))
