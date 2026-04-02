# =========================
# Custom Array Implementation
# =========================
class MyArray:
    """
    Simple array implementation with basic operations:
    insertion, deletion, and access.
    """

    def __init__(self):
        self.data = []  # underlying Python list

    def insert(self, value, index=None):
        """
        Insert value into array.
        If index is None, append at end.
        """
        if index is None:
            self.data.append(value)  # add at end
        else:
            self.data.insert(index, value)  # insert at given index

    def delete(self, index):
        """
        Delete element at specified index.
        """
        return self.data.pop(index)

    def access(self, index):
        """
        Access element at index.
        """
        return self.data[index]


# =========================
# Stack Implementation (using Array)
# =========================
class Stack:
    """
    Stack implementation using Python list.
    Supports push, pop, and peek operations.
    Follows LIFO (Last In, First Out) principle.
    """

    def __init__(self):
        self.items = []

    def push(self, val):
        """
        Push element onto the stack.
        """
        self.items.append(val)

    def pop(self):
        """
        Pop element from the stack. Returns None if empty.
        """
        return self.items.pop() if self.items else None

    def peek(self):
        """
        Return top element without removing it.
        """
        return self.items[-1] if self.items else None


# =========================
# Queue Implementation (using Array)
# =========================
class Queue:
    """
    Queue implementation using Python list.
    Supports enqueue and dequeue operations.
    Follows FIFO (First In, First Out) principle.
    """

    def __init__(self):
        self.items = []

    def enqueue(self, val):
        """
        Add element to the end of the queue.
        """
        self.items.append(val)

    def dequeue(self):
        """
        Remove and return element from front of queue.
        Returns None if queue is empty.
        """
        return self.items.pop(0) if self.items else None


# =========================
# Singly Linked List Implementation
# =========================
class Node:
    """
    Node class for singly linked list.
    Contains value and pointer to next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """
    Singly linked list implementation with basic operations:
    insertion at head/tail, deletion, and traversal.
    """

    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        """
        Insert new node at the head of the list.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        """
        Insert new node at the tail of the list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, value):
        """
        Delete first occurrence of value in the list.
        """
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def traverse(self):
        """
        Print all elements of the list.
        """
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")


# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    print("=== Arrays ===")
    arr = MyArray()
    arr.insert(10)
    arr.insert(20)
    print("Access index 0:", arr.access(0))
    arr.delete(0)
    print("Array after deletion:", arr.data)

    print("\n=== Stack ===")
    s = Stack()
    s.push(5)
    s.push(10)
    print("Top element:", s.peek())
    print("Popped element:", s.pop())

    print("\n=== Queue ===")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Dequeued element:", q.dequeue())

    print("\n=== Singly Linked List ===")
    ll = SinglyLinkedList()
    ll.insert_at_head(10)
    ll.insert_at_tail(20)
    ll.traverse()
    ll.delete(10)
    ll.traverse()