'''
    Collection of exercises about the fundamentals of Python for revision and prep. Includes basic algorithms and
    LeetCode algorithm exercises. A mix of easy, medium and hard questions.
    They are prep interview questions technical skill development for understanding.
'''

# =================================================================================================================== #
                                           # Exercise 1 -
'''
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded 
    by ones at both ends in the binary representation of N. For example, number 9 has binary representation 1001 
    and contains a binary gap of length 2, given N = 1041 the function should return 5, because N has binary 
    representation 10000010001 and so its longest binary gap is of length 5
    
'''

def binary_gap(n):
    # format the number into binary
    binary = '{0:04b}'.format(n)
    # print(binary)
    # strip the outside 0's, creating substring of inside 0's split by one
    max_gap = binary.strip('0').split('1')
    # return the largest 0 substring
    return max([len(i) for i in max_gap])

print(binary_gap(1041))


# =================================================================================================================== #
                                           # Exercise 2 - Passing Cars
'''
    A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive 
    cars on a road.
    
    Array A contains only 0s and/or 1s:
    
    0 represents a car traveling east,
    1 represents a car traveling west.
    The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is 
    traveling to the east and Q is traveling to the west.
    
    For example, consider array A such that:
    
      A[0] = 0
      A[1] = 1
      A[2] = 0
      A[3] = 1
      A[4] = 1
    We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4)
    The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000
'''

def solution(a):
    # count how many elements (0's & 1's) each element has. if 0 check the left, if 1 check right
    # track movement of 0's and 1's. P must be less than Q to be passing
    count = 0
    passes = 0
    for i in a:
        if i == 0:
            count += 1
        else:
            passes += count
        # handle max passing cars
        if i > 1000000000:
            return - 1
    return passes


a = [0, 1, 0, 1, 1]
print(solution(a))

# =================================================================================================================== #
                                       # Exercise 3 - Find smallest positive integer
'''
    You are given an unsorted array with both positive and negative elements. You have to find the smallest positive 
    number missing from the array in O(n) time using constant extra space. You can modify the original array.
    
    Example:
    Input:  {2, 3, 7, 6, 8, -1, -10, 15}
    Output: 1
'''

def smallest_posit_int(a):
    if len(a) == 0:
        return 0
    # sort array to increase O(n)
    a.sort()
    smallest = 1
    for i in a:
        if smallest in a:
            smallest += 1
    return smallest

# a = [2, 3, 7, 6, 8, -1, -10, 15]
a = [1, 2, 3, 6, 10, 5, 8] # output = 4
print(smallest_posit_int(a))
