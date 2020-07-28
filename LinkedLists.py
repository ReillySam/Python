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

# ========================================= Doubly Linked Lists ==================================================
'''
    Implement a doubly linked list that can iterate in both forward and backward directions.
    Implement methods to insert and remove data at a given index or given value.
'''

class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # create new node and make the head(beginning) the new node
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        # if head is empty, make new node the first node (both beginnign/end node)
        if self.head is None:
            self.head = Node(data, None)
            return
        # otherwise, iterate from head to end node and make empty node equal to new node
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_new_values(self, data_list):
        # create new linked list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, value_after, data):
        if self.head is None:
            return
        if self.head.data == value_after:
            self.head.next = Node(data, self.head.next)

        itr = self.head
        while itr.next:
            if itr.data == value_after:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head.data = self.head.next

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        # iterate through list and print data string
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(23)
    ll.insert_at_end(12)
    ll.insert_at_end(999)
    ll.insert_values([22,44,88])
    ll.print_forward()
    ll.insert_new_values(["Apple", "Mango", "Orange", "Banana"])
    ll.print_forward()
    ll.insert_at(0, "Peach")
    ll.print_forward()
    print("Linked List length:",ll.get_length())
    ll.remove_at(2)
    ll.print_forward()
    ll.insert_at(1, "Kiwi")
    ll.print_forward()
    ll.insert_after_value("Apple", "Plum")
    ll.remove_by_value("Kiwi")
    ll.remove_by_value("Banana")
    ll.print_forward()

# ====================================================================================================================

'''
    Created two neew classes to represent the Doubly linked list implementations 
'''

class NodeDLL:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + ' --> '
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = NodeDLL(data, self.head, None)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index== 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    print("____________________________________ DOUBLY LINKED LIST ____________________________________________________")
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
    ll.print_backward()
