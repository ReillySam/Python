# =================================== Exercise 1 =================================== #
# How many three-digit numbers are divisible by 17? Write a program to print them.

# count = 0
# divisible = []
# for i in range(1,1000):
#     if i % 17 == 0:
#         count += 1
#         divisible.append(i)
# print(count, ":", divisible)


# =================================== Exercise 2 =================================== #
# Write a program that prompts for an integer — let’s call it X — and then finds the
# sum of X consecutive integers starting at 1. That is, if X = 5, you will find the sum
# of 1 + 2 + 3 + 4 + 5 = 15.

# integer = int(input("Input an integer: "))
# sum = 0
# for i in range(1, integer + 1):
#    sum += i
# print(sum)

# Modify your program by enclosing your loop in another loop so that you can find
# consecutive sums.

# integer = int(input("Input an integer: "))
#
# for i in range(1, my_int + 1):
#    sum = 0
#    for j in range(1, i + 1):
#        sum += j
#        if (j < i):
#            print(j, " + ", end= "")
#        else:
#            print(j, " = ", end= "")
#    print(sum)

# Modify your program again to only print sums if the sum is divisible by the number
# of operands.

# integer = int(input("Input an integer: "))
#
# for i in range(2, integer + 1, 2):
#     sum = 0
#     count = 1
#     result = ""
#     for j in range(1, i + 1):
#         sum += j
#         count += 1
#         if j < i:
#             result += str(j) + " + "
#         else:
#             result += str(j) + " ="
#
#     if sum % count == 0:
#         print (result, sum)

# =================================== Exercise 3 =================================== #
# Suppose you have a string ab_string = 'abababababababab' . Write an
# expression to remove all the b’s and create a string a string = 'aaaaaaaa' .

# ab_string = 'abababababababab'
# b_string = ab_string.replace('b',"")
# print(b_string)

# =================================== Exercise 4 =================================== #
# Write a Python program that will swap two random letters in a string.
# Hint: Random letters means “letters with random index”

# import random
# string = input("Input a string: ")
#
# i = random.randint(0, len(string) -1)
# j = random.randint(0, len(string) -1)
#
# while i >= j:  # re-generates random indexes so slicing will work.
#     i = random.randint(0, len(string) - 1)
#     j = random.randint(0, len(string) - 1)
#
# new_string = string[:i] + string[j] + string[i + 1:j] + string[i] + string[j+1:]  # Reconstruct string with changed letters
# print("Randomised:", new_string)
# print("Changed Characters are:", string[i],",",string[j])


# =================================== Exercise 5 =================================== #
# Pig Latin is a game of alterations played on words. To make the Pig Latin form of an
# English word the initial consonant sound is transposed to the end of the word and an
# “ay” is affixed. Specifically there are two rules:
# (a) If a word begins with a vowel, append “yay” to the end of the word.
# (b) If a word begins with a consonant, remove all the consonants from the beginning
# up to the first vowel and append them to the end of the word. Finally, append “ay”
# to the end of the word

# def pig_latin():
#     word = input("Enter a word: ")
#     while word != "/":
#         vowels = ["a", "e", "i", "o", "u"]
#         if word[0] in vowels:      # If word starts with a vowel just add yay to the end
#             new_word = word + "yay"
#             print("Pig Latin word is '{}'".format(new_word))
#         else:   # If word does not start with a vowel, get the consonants at the beginning
#             consonants = ''
#             index = 0
#             while index < len(word) and word[index] not in vowels:  # Keep iterating until finds a vowel
#                 consonants += word[index]
#                 index += 1
#             new_word = word[index:] + consonants + "ay"
#             print("Pig Latin word is '{}'".format(new_word))
#
#         word = input("Enter another word (press '/' to quite): ")
#     print("Goodbye!!")
#
# pig_latin()


# =================================== Exercise 6 =================================== #
# Write a function that takes a number as a parameter, iterates from 0 to
# that number, and for each iteration of the loop, multiplies the current number by 9
# and prints the result

# def multiplier():
#     number = int(input("Please enter a number: "))
#     multiple = int(input("Enter a number to multiple by: "))
#     for i in range (number + 1):
#         print(i, "x", multiple, "=", i*multiple)
#
#
# multiplier()


# =================================== Exercise 7 =================================== #
# Write a Python function to insert a string in the middle of a string.
# Sample function and result: insert_string_middle(“{{}}”,”PHP”)
# Should return {{PHP}}

# def string_insertion():
#     string1 = input("Input a string: ")
#     string2 = input("Input an abbreviation to insert: ")
#     insertion = string2
#     print(string1[0:len(string1)//2] + insertion + string1[(len(string1)//2):])
#
#
# string_insertion()

# =================================== Exercise 8 =================================== #
# Write a Python function that takes a string and two indices, and returns
# a string with the part between the indices removed

def remove_substring():
    string = input("Write a string: ")
    index1 = int(input("Enter beginning index: "))
    index2 = int(input("Enter ending index to form substring: "))

    substring = string[index1:index2 + 1]
    print(string.replace(substring, ''))


remove_substring()


def remove_substring2(a,b,c):
    '''Compressed version'''
    print(a[:b],end=a[c+1:])


remove_substring2("Hello There", 2, 6)
