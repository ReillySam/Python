# ========================================== Linked Lists =============================================================
'''
    A linked list is a sequence of data elements, which are connected together via links.
    Each data element contains a connection to another data element in form of a pointer.
    Python does not have linked lists in its standard library. We implement the concept of
    linked lists using the concept of nodes.We create a Node object and create another class
    to use this ode object. We pass the appropriate values through the node object to point
    the to the next data elements.

    Types, Traversing, Insertion, deletion, displaying
'''

# ========================================= Singly Linked Lists ===============================================

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = Node()

    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Returns the length (integer) of the linked list.
    def length(self):
        current_node = self.head
        total = 0
        while current_node.next:         # None represents Null, the end of the list
            total += 1
            current_node = current_node.next
        return total

    # Prints out the linked list in traditional Python list format.
    def printList(self):
        elements = []
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length() or index < 0 :
            print("ERROR: index out of range."); return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index: return current_node.data
            current_index += 1

    def delete(self, index):
        if index >= self.length() or index < 0 :
            print("ERROR: index out of range."); return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next; return
            current_index += 1


linked_list1 = LinkedList()
linked_list1.append("A")
linked_list1.append("B")
linked_list1.printList()
linked_list1.append("C")
linked_list1.append("D")
linked_list1.printList()
print(linked_list1.get(2))
print(linked_list1.get(7))
linked_list1.delete(1)
linked_list1.printList()

