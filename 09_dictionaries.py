# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# fhand = open("words.txt")
# dictWords = dict()
#
# for line in fhand:
#     flist = line.split()
#     if len(flist) > 0:
#         for word in flist:
#             dictWords[word] = 1
#
# print("and" in dictWords)

# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and
# keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Error file name %s" %fname)

counts = dict()

for line in fhand:
    line = line.strip()
    lineList = line.split()
    if len(lineList) > 0 and lineList[0] == "From":
        counts[lineList[2]] = counts.get(lineList[2], 0) + 1

print(counts)
