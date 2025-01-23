class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    head: Node
    tail: Node
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        if not value:
            return

        node = Node(value)

        if self.tail:
            self.tail.next = node
            self.tail = node
        
        else:
            self.tail = self.head = node

    def deque(self):
        if self.head:
            current_head = self.head.data
            self.head = self.head.next
            return current_head

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

linked_list = LinkedList()
linked_list.insert("A")
linked_list.insert("B")
linked_list.insert("C")
linked_list.deque()

print("Linked List:")
linked_list.print_list()
