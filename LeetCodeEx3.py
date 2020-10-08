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


# =================================================================================================================== #
                                    # Exercise 4 - Sort by Array Parity
'''
    Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
    followed by all the odd elements of A.
    You may return any answer array that satisfies this condition
'''

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return_arr = []
        odd_elements = []
        for i in A:
            if i % 2 == 0:
                return_arr.append(i)
            else:
                odd_elements.append(i)
        return return_arr + odd_elements


# =================================================================================================================== #
                                    # Exercise 5 - Product of Last Number K
'''
    Implement the class ProductOfNumbers that supports two methods:
    
    1. add(int num)
    Adds the number num to the back of the current list of numbers.
    
    2. getProduct(int k)
    Returns the product of the last k numbers in the current list.
    You can assume that always the current list has at least k numbers
'''
# This solution gives the correct output but very poor time complexity, looking to fix
import numpy

class ProductOfNumbers(object):

    def __init__(self):
        self.number_list = []

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < 0 or num > 100:
            return 0
        self.number_list.append(num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k < 1 or k > 40000:
            return 0
        return numpy.prod(self.number_list[-k:])

# Solid solution
    # def __init__(self):
    #     self.nums = [1]
    #
    # def add(self, num):
    #     if (not num):
    #         self.nums = [1]
    #     else:
    #         self.nums.append(self.nums[-1] * num)
    #
    # def getProduct(self, k):
    #     if (k >= len(self.nums)):
    #         return 0
    #     return self.nums[-1] // self.nums[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


# =================================================================================================================== #
                                    # Exercise 6 - Average of Levels in Binary Tree
'''
    Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
    Example:
    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]
    
    Explanation:
    The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []

        output = []
        queue = collections.deque([root])

        while queue:
            level_sum = 0
            level_nodes = len(queue)
            for _ in range(level_nodes):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append((level_sum / level_nodes))

        return output

# =================================================================================================================== #
                                    # Exercise 7 - Index of dominator in array
'''
    An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than 
    half of the elements of A.
    
    For example, consider array A such that
    
     A[0] = 3    A[1] = 4    A[2] =  3
     A[3] = 2    A[4] = 3    A[5] = -1
     A[6] = 3    A[7] = 3
    The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) 
    and 5 is more than a half of 8.
    
    Write a function:
    def solution(A)
    
    that, given an array A consisting of N integers, returns index of any element of array A in which the dominator 
    of A occurs. The function should return −1 if array A does not have a dominator
'''

def solution(A):
    if len(A) > 100000: return -1
    # first find dominator
    A.sort()
    dominator = []
    counter = 0
    for i in A:
        occurrence = A.count(i)
        if occurrence > counter:
            counter = occurrence
            dominator = i
    if counter <= len(A)/2:
        return -1
    # next find index
    #idx = [A.index(dominator) for i in A]
    return [i for i,x in enumerate(A) if x == dominator]


def solution_2(A):
    dominator = max(set(A), key = A.count)
    return [i for i,x in enumerate(A) if x == dominator]


# This function is not correct, will fix
print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
# Correct, elegant and simple
print(solution_2([3, 4, 3, 2, 3, -1, 3, 3]))


# =================================================================================================================== #
                                    # Exercise 8 - Available captures for Rook
'''
    On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  
    These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and 
    lowercase characters represent black pieces. The rook moves as in the rules of Chess: it chooses one of four cardinal
    directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of 
    the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move
    into the same square as other friendly bishops.
    
    Return the number of pawns the rook can capture in one move
    
    Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],
    [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    Output: 3
'''


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        captures = 0
        rook_index = (0, 0)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'R':
                    rook_index = (row, col)
                    break

        # check left
        flag = True
        pawn = 0
        col = rook_index[1] - 1
        while col >= 0:
            if board[rook_index[0]][col] == 'B':
                flag = False
                break
            if board[rook_index[0][col] == 'p':
            pawn + 1
                break
            col -= 1
        if flag and pawn != 0:
            captures += 1

        # check right
        flag = True
        pawn = 0
        col = rook_index[1] + 1
        while col < len(board[0]):
            if board[rook_index][col] == 'B':
                flag = False
                break
            if board[rook_index][col] == 'p':
                pawn + 1
                break
            col += 1
        if flag and col != 0:
            captures += 1

        # check down
        flag = True
        pawn = 0
        row = rook_index[0] + 1
        while row < len(board):
            if board[row][rook_index[1]] == 'B':
                flag = False
                break
            if board[rook_index][col[1]] == 'p':
                pawn += 1
                break
            col += 1
        if flag and col != 0:
            captures += 1

        # check up
        flag = True
        pawn = 0
        row = rook_index[0] - 1
        while row >= 0:
            if board[row][rook_index[1]] == 'B':
                flag = False
                break
            if board[rook_index][col[1]] == 'p':
                pawn += 1
                break
            col += 1
        if flag and col != 0:
            captures += 1

        return captures
