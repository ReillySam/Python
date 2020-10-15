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
                                         # Exercise 5 - Strobogrammatic Numbers
'''
    Write a Python program to get all strobogrammatic numbers that are of length n. Go to the editor
    A strobogrammatic number is a number whose numeral is rotationally symmetric, so that 
    it appears the same when rotated 180 degrees. In other words, the numeral looks the same 
    right-side up and upside down (e.g., 69, 96, 1001).
'''

def strobogrammatic(n):
