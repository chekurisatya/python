'''
 Using deque for Queue Operations
Implement a class Queue that uses collections.deque to perform standard queue operations: enqueue, dequeue, size, and is_empty.
'''
from collections import deque

class Queue:
    def __init__(self):
        # Initialize the deque here
        self.D = deque()

    def enqueue(self, item):
        # Add an item to the queue
        self.D.append(item)

    def dequeue(self):
        # Remove and return the front item from the queue
        return self.D.popleft()

    def size(self):
        # Return the size of the queue
        return len(self.D)

    def is_empty(self):
        # Return whether the queue is empty or not
        return True if len(self.D) == 0 else False

# Test the queue implementation
#
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.is_empty())