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
    # strip the outside 0's, creating substring of inside 0's split by one
    max_gap = binary.strip('0').split('1')
    # return the largest 0 substring
    return max([len(i) for i in max_gap])

print(binary_gap(100))
