'''
    Collection of exercises about the fundamentals of Python for revision and prep. Includes basic algorithms and
    LeetCode algorithm exercises. A mix of easy, medium and hard questions.
    They are prep interview questions technical skill development for understanding.
'''

# =================================================================================================================== #
                                        # Exercise 1 - Best time to buy & sell stock
'''
    Say you have an array for which the ith element is the price of a given stock on day i.
    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
    design an algorithm to find the maximum profit. Note that you cannot sell a stock before you buy one
'''

# def maxProfit(prices):
#     left_pointer = 0
#     profit = 0
#     if len(prices) == 0:
#         print("No stock prices available")
#     else:
#         for index, price in enumerate(prices):
#             if price < prices[left_pointer]:
#                 left_pointer = index
#             elif price > prices[left_pointer]:
#                 profit = max(profit, price - prices[left_pointer])
#         print("Max profit = {0}".format(profit))
#
#
# maxProfit([])
# maxProfit([5, 1 , 3, 9, 7])


# =================================================================================================================== #
                                    # Exercise 2 - Simple status ouputs
'''
    Write a Python program to get the Python version you are using.
    Write a Python program to display the current date and time.
'''

# import sys
# import datetime
#
# class PythonStatus(object):
#
#     def systemVersion(self):
#         print("System version:\n",sys.version)
#
#     def dateTime(self):
#         print("Current date and time:\n",datetime.datetime.now())
#
# python = PythonStatus()
# python.systemVersion()
# python.dateTime()


# =================================================================================================================== #
                                    # Exercise 3 - Divisible

'''
    Write a Python function to check whether a number is divisible by another number. 
    Accept two integers values form the user.
'''

# def divisibleCheck():
#     while 1:
#         try:
#             number_1 = float(input("Enter the first number: "))
#             number_2 = float(input("Enter the second number: "))
#             result = number_1 / number_2
#             if number_1 % number_2 == 0:
#                 print("{} is divisible by {}\nAnswer = {}".format(number_1,number_2,result))
#                 break
#             else:
#                 print("{} is NOT divisible by {}\nAnswer = {}".format(number_1,number_2,result))
#                 break
#         except:
#             print(ValueError, "Be sure to enter an integer.")
#
#
# divisibleCheck()


# =================================================================================================================== #
                                    # Exercise 4 - Odd Product
'''
    Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.
'''

# def oddProduct(integer_values):
#     for i in integer_values:
#         for j in integer_values:
#             if i != j:
#                 result = i * j
#                 if result % 2 == 0:
#                     continue
#                 else:
#                     print("Odd Product found - {} : {} x {}".format(result, i, j))
#
#
# numbers1 = [2,4,6,8,10]
# numbers2 = [1,4,7,8,10]
#
# print(oddProduct(numbers1))
# oddProduct(numbers2)


# =================================================================================================================== #
                                    # Exercise 5 - Strobogrammatic Numbers
'''
    Write a Python program to get all strobogrammatic numbers that are of length n. Go to the editor
    A strobogrammatic number is a number whose numeral is rotationally symmetric, so that 
    it appears the same when rotated 180 degrees. In other words, the numeral looks the same 
    right-side up and upside down (e.g., 69, 96, 1001).
'''

# def genStrobogrammatic(n):
#     result = stroboNumber(n, n)
#     return result
#
#
# def stroboNumber(n, length):
#     if n == 0:
#         return [""]
#     if n == 1:
#         return ["1", "0", "8"]
#     middles = stroboNumber(n-2, length)  # Recursion
#     result = []
#     for middle in middles:
#         if n != length:
#             result.append("0" + middle + "0")
#         result.append("8" + middle + "8")
#         result.append("1" + middle + "1")
#         result.append("9" + middle + "6")
#         result.append("6" + middle + "9")
#     return result
#
# print("n = 2:\n",genStrobogrammatic(1))
# print("n = 2:\n",genStrobogrammatic(2))
# print("n = 3:\n",genStrobogrammatic(3))
# print("n = 4:\n",genStrobogrammatic(4))
#
#
# def isStrobogramamtic(n):
#     # Quick way to check if a number is or is not a Strobogrammatic number
#     map = {
#         '0' : '0',
#         '1' : '1',
#         '6' : '9',
#         '8' : '8',
#         '9' : '6',
#     }
#
#     left = 0
#     right = len(n) - 1
#     while left <= right:
#         if n[left] not in map or n[right] not in map:
#             return False
#         if n[left] != map[n[right]]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
#
# print(isStrobogramamtic('10'))
# print(isStrobogramamtic('101'))


# =================================================================================================================== #
                                    # Exercise 7 - Webscrape
'''
    Write a Python program to get the top news stories from BBC news
'''

import requests


# def NewsFromBBC():
#     # BBC news api
#     main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
#
#     # fetching data in json format
#     open_bbc_page = requests.get(main_url).json()
#
#     # getting all articles in a string article
#     article = open_bbc_page["articles"]
#     results = []
#
#     for ar in article:
#         results.append(ar["title"])   # index and appends only Titles
#     print("==================================   Todays News   ==================================")
#     for i in range(len(results)):
#         print(i + 1, results[i])
#
# # Driver Code
# if __name__ == '__main__':
#     NewsFromBBC()


# =================================================================================================================== #
                                                # Exercise 8 
    '''
    Write a Python program to compute the sum of all items of a given array of integers where each integer is
    multiplied by its index. Return 0 if there is no number.
'''

# def sum_index_multiplier(numbers):
#     for i,j in enumerate(numbers):
#         print(i,'x',j,'=',i*j)
#     print((sum(i*j for i, j in enumerate(numbers))))
#
# sum_index_multiplier([1,2,3,4,5])


# =================================================================================================================== #
                                                # Exercise 9 Isomorphic Strings
'''
    In abstract algebra, a group isomorphism is a function between two groups that sets up a one-to-one 
    correspondence between the elements of the groups in a way that respects the given group operations. 
    If there exists an isomorphism between two groups, then the groups are called isomorphic.
    Two strings are isomorphic if the characters in string A can be replaced to get string B
'''
#
# def isIsomorphic(string_1, string_2):
#     dict_string1 = {}
#     dict_string2 = {}
#
#     if len(string_1) == 0 or len(string_2) == 0 or len(string_1) != len(string_2):
#         print(False)
#     for i, value in enumerate(string_1):
#         dict_string1[value] = dict_string1.get(value, []) + [i]
#     for j, value in enumerate(string_2):
#         dict_string2[value] = dict_string2.get(value, []) + [j]
#     if sorted(dict_string1.values()) == sorted(dict_string2.values()):
#         print(True)
#     print(False)
#
# def inputStrings():
#     string_1 = input("Enter the first string: ")
#     string_2 = input("Enter the first string: ")
#     isIsomorphic(string_1, string_2)
#
# inputStrings()



class Solution(object):

    def isIsomorphic(self, string_1, string_2):
        if (string_1 or string_2) is None or len(string_1) != len(string_2):
            return False
        # dict used to map characters from each string
        dict = {}
        # use to check already mapped characters
        s = set()

        for i, a in enumerate(string_1):
            dict[a] = string_1[i]
            b = string_2[i]

            # return false if a is seen already and mapped to diff character
            if dict[a] != b:
                return False
            else:
                # if not seen before and has not been mapped
                if b in s:
                    return False
            # otherwise map characters together
            dict[a] = b
            s.add(b)
        return True


isomorphic_strings = Solution()
print(isomorphic_strings.isIsomorphic("paper", "title"))
print(isomorphic_strings.isIsomorphic("foo", "bar"))
print(isomorphic_strings.isIsomorphic("aab", "xxy"))

# =================================================================================================================== #
                                        # Exercise 10 Goldbach's conjecture numbers
'''
    Write a Python program that accepts an even number (>=4, Goldbach number) from the user and 
    creates a combination that express the given number as a sum of two prime numbers. Print 
    the number of combinations. Goldbach number: A Goldbach number is a positive even integer that 
    can be expressed as the sum of two odd primes.[4] Since four is the only even number greater 
    than two that requires the even prime 2 in order to be written as the sum of two primes, 
    another form of the statement of Goldbach's conjecture is that all even integers greater 
    than 4 are Goldbach numbers
'''


def primeNumberList(integer_input):
    # create a list to append all prime numbers to
    prime_numbers = [2]
    # all odd integers
    for i in range(3, integer_input, 2):
        # check if integers have factors
        for j in range(2, i):
            if i%j == 0:
                break
            elif j == i - 1:
                prime_numbers.append(i)
    return prime_numbers


def goldbachNumbers(prime_numbers):
    # checks all even nums up to the number
    for i in range(4, 100, 2):
        for number_1 in prime_numbers:
            # minus prime number from even num and check if remainder is in the prime num list
            number_2 = i - number_1
            if number_2 in prime_numbers:
                a,b,c = i,number_1,number_2
                print(a,'=',b,'+',c)
                break


def main():
    integer_input = int(input("Enter an upper limit integer to check Goldbach's Conjecture: "))
    list = primeNumberList(integer_input)
    goldbachNumbers(list)


main()
