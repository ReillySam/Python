# =============================================== Binary Trees =======================================================
'''
    A binary tree is a data structure in which every node or vertex has at most two children.
    In Python, a binary tree can be represented in different ways with different data
    structures(dictionary, list) and class representation for a node. Nodes may contain two
    children nodes, left and/or right. All contain a root node.

    Binary Search Tree - All nodes to right right must be larger and all nodes to the left must
    be smaller than the root/parent node(s)

    Insert, Delete, Traverse, Search, Validate
'''

import sys

class Nodes():
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)
        else:
            return None

    def _printTree(self, current_node):
        if current_node != None:
            self._printTree(current_node.left_child)
            print(str(current_node.value))
            self._printTree(current_node.right_child)

    def insert(self, value):
        if self.root == None:
            self.root = Nodes(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Nodes(value)
                current_node.left_child.parent = current_node
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = Nodes(value)
                current_node.right_child.parent = current_node
            else:
                self._insert(value, current_node.right_child)
        else:
            print("Value already in tree!")

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None: return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child != None:
            return self._find(value, current_node.left_child)
        elif value < current_node.value and current_node.right_child != None:
            return self._find(value, current_node.right_child)

    def deleteValue(self, value):
        return self.deleteNode(self.find(value))

    def deleteNode(self, node):
        # returns node with min value in tree rooted at the input node
        def minValueNode(n):
            current_node = n
            while current_node.left_child != None:
                current_node = current_node.left_child
                return current_node

        # returns number of children on specified node
        def numChildren(n):
            num_children = 0
            if n.left_child != node: num_children += 1
            if n.right_child != node: num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent
        # get the children of the node to be deleted
        node_children = numChildren(node)

        # break operation into 3 cases based on structure of tree and nodes to be deleted
        # CASE 1: node has no children
        if node_children == 0:
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # CASE 2: node has 1 child
        if node_children == 1:
            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            # replace the node to be deleted with its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3: node ahs 2 children
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = minValueNode(node.right_child)
            # copy the inorder successor to the node formerly holding the value that has been deleted
            node.value = successor.value
            # delete the inorder successor now that its value has been copied into the others place
            self.deleteNode(successor)


    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)
        else:
            return False



def fillTree(tree, num_elems = 100, max_int = 1000):
    from random import randint
    for _ in range(num_elems):
        current_elems = randint(0, max_int)
        tree.insert(current_elems)
    return tree


def validateBST(root, min =- sys.maxint, max = sys.maxint):
    # if current node is none
    if root == None:
        return True
    # 4 operations need to return true for function to pass
    # ensure current node value is greater than the min set value and current node value is less than max set value
    if (root.value > min and
        root.value < max and
        # recursively call. pass left child of current node as root, propagate on same min value as next min value
        # then pass on current node as the next max value. Constrains all nodes to left from having any values
        # greater than or equal to the current node value
        validateBST(root.left_child, min, root.value) and
        # pass right child of current node as root. Pass current node value as min value and propagate on same
        # max value. Constrains all nodes to right from having any values less than or equal to the current node
        # value
        validateBST(root.right_child, root.value, max)):
        return True
    else:
        return False


tree = BinarySearchTree()
# tree = fillTree(tree)
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)
tree.insert(20)

tree.printTree()
print("Tree height: "+str(tree.height()))
print(tree.search(5))
print(tree.search(30))
print("==========================================================")
print(tree.deleteValue(10))
tree.printTree()
print(tree.deleteValue(3))
tree.printTree()
print(tree.deleteValue(7))
tree.printTree()

