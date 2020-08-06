# =============================================== Stacks & Queues =====================================================
'''
    Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO)
    principle. Queue is a container of objects (a linear collection) that are inserted and removed according
    to the first-in first-out (FIFO) principle
'''

# ==================================================== Stacks =========================================================
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def getStack(self):
        return self.items

stack1 = Stack()
stack1.push('A')
stack1.push('B')
stack1.push('X')
stack1.push('Z')
print(stack1.getStack())
stack1.pop()
print(stack1.getStack())
print(stack1.isEmpty())
print(stack1.peek())


'''
    Use a stack to check whether a string has a balanced usage of parenthesis or not. 
    Example:
    (), (()), (({})) - Balanced
    ((), {{()}}], - Not balanced 
'''

def isParenBalanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '({[':
            s.push(paren)
        else:
            if s.isEmpty():
                is_balanced = False
            else:
                top = s.pop()
                if not isMatch(top , paren):
                    is_balanced = False
        index += 1
    if s.isEmpty() and is_balanced: return True
    else: return False


def isMatch(p1, p2):
    if p1 == '(' and p2 == ')': return True
    elif p1 == '{' and p2 == '}': return True
    elif p1 == '[' and p2 == ']': return True
    else: return False


print(isParenBalanced("()"))
print(isParenBalanced("([)"))
print(isParenBalanced("({[]})"))
print("_______________________________________________________________________________________________________________")



# ==================================================== Queues =========================================================

from collections import deque


class Queue():

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})


for i in pq.buffer: print(i)
print(pq.size())
pq.dequeue()
for i in pq.buffer: print(i)

print("_______________________________________________________________________________________________________________")


'''
    Design a food ordering system where your python program will run two threads,
    
    Place Order: This thread will be placing an order and inserting that into a queue. This thread places new 
    order every 0.5 second. (hint: use time.sleep(0.5) function)
    
    Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and
    print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order 
    thread is started.
'''

import time
import threading

order_queue = Queue()

def placeOrder(orders):
    for order in orders: order_queue.enqueue(order) and print("\nYour order has been placed: ", order)
    for i in order_queue.buffer: print("Order list: ",i)
    print( "_____________________________________________________________________________________________________")
    time.sleep(0.5)

def serveOrder():
    time.sleep(2)
    while True:
        if order_queue.isEmpty():
            print("\nNo more food left")
            break
        order_served = order_queue.dequeue()
        print("\nOrder ready!! >>>>>",order_served)
        time.sleep(2)


# if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    print("Todays Menu: ",orders)

    t1 = threading.Thread(target = placeOrder, args = (orders, ))
    t2 = threading.Thread(target= serveOrder)

    t1.start()
    t2.start()


'''
    Write a program to print binary numbers from 1 to 10 using Queue.Hint: Notice a pattern above. After 1 second 
    and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number
    (i.e. 10) + 1.
'''

def binaryNumbers(n):
    bn_queue = Queue()
    bn_queue.enqueue("1")

    for i in range(n):
        front = bn_queue.front()
        print(front)
        bn_queue.enqueue(front + "0")
        bn_queue.enqueue(front + "1")

        bn_queue.dequeue()

if __name__ == '__main__':
    binaryNumbers(10)
