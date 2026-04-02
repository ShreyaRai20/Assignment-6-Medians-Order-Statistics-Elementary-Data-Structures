"""
Stack and Queue using arrays
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """Add element to top"""
        self.stack.append(value)

    def pop(self):
        """Remove top element"""
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        """View top element"""
        return self.stack[-1] if self.stack else None


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """Add element to rear"""
        self.queue.append(value)

    def dequeue(self):
        """Remove front element"""
        if self.queue:
            return self.queue.pop(0)
        return None

    def front(self):
        return self.queue[0] if self.queue else None