'''
                                                --- Revision ---
    Small file to practice questions, algorithms and coding techniques.
    Exercises taken from previous interview questions and projects.
'''

# ====================================================================================================================
                                                # Bubble Sort

# Bubble sorting algorithm that compares an element and its next element, swapping elements. Smallest to the left.
def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

l = [3,15,7,1,19,44,2,5,0]
# print(bubble_sort(l))



# =================================================================================================================== #
                                            # Goldbach's conjecture numbers
'''
    Write a Python program that accepts an even number (>=4, Goldbach number) from the user and 
    creates a combination that express the given number as a sum of two prime numbers. Print 
    the number of combinations. Goldbach number: A Goldbach number is a positive even integer that 
    can be expressed as the sum of two odd primes.[4] Since four is the only even number greater 
    than two that requires the even prime 2 in order to be written as the sum of two primes, 
    another form of the statement of Goldbach's conjecture is that all even integers greater 
    than 4 are Goldbach numbers
    
    Sort all prime numbers up to number. Find all even numbers up to number. See if the factor of 
    even - prime is in prime nums list.
'''

def prime_numbers(integer):
    prime_nums = [2]
    for i in range(3, integer, 2):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i - 1:
                prime_nums.append(i)
    return prime_nums

def goldbach_nums(prime_numbers, integer):
    for even in range(4, integer, 2):
        for prime in prime_numbers:
            gb_num = even - prime
            if gb_num in prime_numbers:
                print(even, '=', prime, '+', gb_num)
                break


def main():
    integer = int(input("Enter the integer limit: "))
    prime_nums = prime_numbers(integer)
    goldbach_nums(prime_nums, integer)

main()
