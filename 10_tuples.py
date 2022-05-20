# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("Error file name!")
    exit()

addressDict = dict()

for line in fhand:
    line = line.rstrip()
    line = line.split()
    if len(line) > 0 and line[0] == "From":
        address = line[1]
        addressDict[address] = addressDict.get(address, 0) + 1

addressList = list()

for key in addressDict:
    addressList.append((addressDict[key], key))

addressList.sort(reverse = True)
a, b = addressList[0]

print(b, a)
