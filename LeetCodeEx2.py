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
# import collections

# class Solution():

#     def sumOfLeftLeaves(self, root):
#         if not root:
#             return 0

#         queue = collections.deque()
#         queue.append((root))
#         count = 0
#         while queue:
#             node = queue.popleft()

#             if node.left:
#                 queue.append(node.left)
#                 if not node.left.left and not node.left.right:
#                     count += node.left.val

#             if node.right:
#                 queue.append(node.right)
#         return count


# binary_tree = Solution()
# print(binary_tree.sumOfLeftLeaves(3))


# =================================================================================================================== #
                                            # Exercise 6 - Baseball Game
'''
    You're now a baseball game point recorder.
    Given a list of strings, each string can be one of the 4 following types:
    
    1. Integer (one round's score): Directly represents the number of points you get in this round.
    2. "+" (one round's score): Represents that the points you get in this round are the sum of the last two 
    valid round's points.
    3. "D" (one round's score): Represents that the points you get in this round are the doubled data of the last 
    valid round's points.
    4. "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were
    invalid and should be removed.
    
    Each round's operation is permanent and could have an impact on the round before and the round after.
    You need to return the sum of the points you could get in all the rounds
    
    Input: ["5","2","C","D","+"]
    Output: 30
'''

# class Solution():
#     def cal_points(self, ops):
#         points = []
#         for i in range(len(ops)):
#             try:
#                 if ops[i] == 'C':
#                     points.pop(-1)
#                 elif ops[i] == 'D':
#                     points.append(points[-1] * 2)
#                 elif ops[i] == '+':
#                     points.append(points[-1] + points[-2])
#                 else:
#                     points.append(int(ops[i]))
#             except:
#                 Exception("Invalid operation.")
#         return sum(points)
#
# if __name__ == "__main__":
#     baseball_game = Solution()
#     print(baseball_game.cal_points(["5","2","C","D","+"]))


# =================================================================================================================== #
                                        # Exercise 7 - Arranging coins
'''
    You have a total of n coins that you want to form in a staircase shape, where every k-th row must
    have exactly k coins. Given n, find the total number of full staircase rows that can be formed. 
    'n' is a non-negative integer and fits within the range of a 32-bit signed integer.
'''

# class Solution():
#     def arrange_coins(self, n):
#         '''
#         current coin (row) increments as the remaining value of n decrease. Trade of then as curr > remaining
#         :param n:
#         :return: current coin
#         '''
#         if n == 0:
#             return None
#
#         cur_coin = 1
#         remaining = n - 1 # -1 ensures an incomplete row wont be valid
#
#         while remaining >= cur_coin + 1:  # +1 because each row must have more coins than the last
#             cur_coin += 1
#             remaining = remaining - cur_coin
#         return cur_coin
#
#
# if __name__ == "__main__":
#     coins = Solution()
#     print(coins.arrange_coins(5))
#     print(coins.arrange_coins(8))


# =================================================================================================================== #
                                        # Exercise 8 - Assign Cookies
'''
    Assume you are an awesome parent and want to give your children some cookies. But, you should give each child 
    at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child
    will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
    and the child i will be content. Your goal is to maximize the number of your content children and output the 
    maximum number.
    
    Note:
    You may assume the greed factor is always positive.
    You cannot assign more than one cookie to one child
    '''

# class Solution():
#     def find_content_children(self, g, s):
#         '''
#         match cookies size and child greed by sorting both and decrementing until either hits 0
#         if cookie size does not match greedy child move onto next greedy child
#         :param g:
#         :param s:
#         :return: int
#         '''
#         if s is None: return 0
#         if g is None: return "No children"
#
#         g.sort()
#         s.sort()
#         children = len(g) - 1
#         cookies = len(s) - 1
#         content_child = 0
#         while children >= 0 and cookies >= 0:
#             if s[cookies] >= g[children]:
#                 content_child += 1
#                 cookies -= 1
#                 children -= 1
#             else:
#                 children -= 1
#         return "Content Children: {}".format(content_child)
#
# if __name__ == "__main__":
#     parent = Solution()
#     print(parent.find_content_children([1, 2, 3], [1, 1]))
#     print(parent.find_content_children([1, 2], [1, 2, 3]))


# =================================================================================================================== #
                                        # Exercise 9 - N-ary Tree Postorder Traversal
'''
    Given an n-ary tree, return the postorder traversal of its nodes' values. Nary-Tree input serialization is 
    represented in their level order traversal, each group of children is separated by the null value (See examples).
    
    Recursive solution is trivial, could you do it iteratively?
'''

class Node():
    def __init__(self):
        self.val = None
        self.children = None

class Solution():
    def post_order_recur(self, root):
        # post order traversal using recursion
        result = list()
        self.append_node(root, result)
        return result

    def append_node(self, root, result):
        if not root:
            return None

        for child in root.children:
            self.append_node(child, result)

        result.append(root.val)

    def post_order_iter(self, root):
        # post order traversal using iteration and stack
        result = list()
        if not root:
            return result

        stack = list()
        stack.append(root)

        while stack:
            node = stack.pop()
            result.insert(0, node.val)
            for child in node.children:
                stack.append(child)

        return result

if __name__ == "__main__":
    tree_data = Solution()
    # problem used 'null' to separated each group of children. Not sure how too pass that here. Solution passed on Leetcode
    print(tree_data.post_order_iter([1,null,3,2,4,null,5,6]))
    print(tree_data.post_order_recur([1,null,3,2,4,null,5,6]))
    
