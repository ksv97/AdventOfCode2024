from statistics import quantiles


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.quantity = 0

    def append(self, value: int):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            new_node = Node(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node
        self.quantity += 1

    def insert(self, current, value ):
        # вставка в начало
        new_node = Node(value)
        if current == self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
        self.quantity += 1


    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
