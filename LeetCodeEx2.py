'''
    Collection of exercises about the fundamentals of Python for revision and prep. Includes basic algorithms and
    LeetCode algorithm exercises. A mix of easy, medium and hard questions.
    They are prep interview questions and technical skill development for understanding.
'''


# =================================================================================================================== #
                                        # Exercise 1 - Validate employee code
'''
    Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits. 
    Return True if the employee code is valid and False if it's not.
'''

# class Solution(object):
#     def validateEmployeeCode(self, code):
#         return [len(code) in [8, 12] and code.isdigit()]
#
#     def inputCode(self):
#         code = input("Enter employee code ('q' to quit): ")
#         print(self.validateEmployeeCode(code))
#
#         while code != 'q':
#             code = input("Try again ('q' to quit): ")
#             print(self.validateEmployeeCode(code))
#
#
# emply1 = Solution()
# emply1.inputCode()
# print(emply1.validateEmployeeCode('12345678'))
# print(emply1.validateEmployeeCode('123678'))
# print(emply1.validateEmployeeCode('1b345a78'))
# print(emply1.validateEmployeeCode('123456789123'))


# =================================================================================================================== #
                                        # Exercise 2 - Mask String
'''
     Write a Python program to replace all but the last five characters of a given string into "*" 
     and returns the new masked string.
'''

# class Solution():
#     def maskString(self, string):
#         return '*'*(len(string)-5) + string[-5:]
#
#     def maskString2(self,string):
#         new_string = string[:-5]
#         for i in new_string:
#             new_string = new_string.replace(i, '*')
#         return new_string + string[-5:]
#
#
# masked_string = Solution()
# print(masked_string.maskString("samreilly12345"))
# print(masked_string.maskString2("marypoppins99999"))
# print(masked_string.maskString2("aardvark"))


# =================================================================================================================== #
                                        # Exercise 3 - Increasing Num Trend
'''
    Write a Python program to check whether a sequence of numbers has an increasing trend or not.
'''

# def increasingTrend(sequence):
#     count = 0
#     for num in sequence:
#         if num > count:
#             count = num
#         else:
#             return False
#     return True
#
# def increasingTrend2(sequence):
#     if sorted(sequence) == sequence:
#         return True
#     return False
#
#
# print(increasingTrend([1,2,4,3,8]))
# print(increasingTrend([1,2,4,5,8]))
# print(increasingTrend2([10,20,25,40,50]))
# print(increasingTrend2([1,20,4,30,35]))


# =================================================================================================================== #
                                                # Exercise 4 - Is Parallel
'''
    Write a Python program to check whether two given lines are parallel or not.
    Note: Parallel lines are two or more lines that never intersect. Parallel Lines are like railroad 
    tracks that never intersect. The General Form of the equation of a straight line is: ax + by = c
'''

# def areParallel(line_1, line_2):
#     return (line_1[0] / line_1[1] == line_2[0] / line_2[1])
#
#
# print(areParallel([2,3,4], [2,3,8]))
# print(areParallel([2,3,4], [4,-3,8]))



# =================================================================================================================== #
                                            # Exercise 5 - Sum of left leaves
'''
    Find the sum of all left leaves in a given binary tree.

            3
           / \
          9  20
            /  \
           15   7

    There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
import collections

class Solution():

    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        queue = collections.deque()
        queue.append((root))
        count = 0
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                if not node.left.left and not node.left.right:
                    count += node.left.val

            if node.right:
                queue.append(node.right)
        return count


binary_tree = Solution()
print(binary_tree.sumOfLeftLeaves(3))
