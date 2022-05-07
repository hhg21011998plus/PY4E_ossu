# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

# myString = input("Enter a string: ")
# myIndex = len(myString) - 1
#
# while myIndex >= 0:
#     print("\n", myString[myIndex])
#     myIndex -= 1
#
# print(dir(myString))

# Exercise 2: Given that fruit is a string, what does fruit[:] mean?

# fruit = "banana"
# print(fruit)

# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

myWord = input("Enter a word: ")
myCharacter = input("Enter a character: ")

def count(word, character):
    count = 0
    for letter in word:
        if letter == character:
            count = count + 1
    return count

print("Character", myCharacter, "in", myWord, "=", count(myWord, myCharacter))
