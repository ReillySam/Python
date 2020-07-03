'''
    Collection of exercises about the fundamentals of Python for revision and prep. Includes basic and
    LeetCode algorithm exercises. Beginning with easy questions, then medium and hard.
    Some are prep interview questions or technical skill development and /or understanding based.
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