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

    # def insert(self, data):
    #     if not self.head:
    #         self.head = Node(data)
    #     else:
    #         current_node = self.head
    #         while current_node.next:
    #             current_node = current_node.next
    #         current_node.next = Node(data)


    def insert(self, value):
        if not value:
            return

        node = Node(value)

        if self.tail:
            self.tail.next = node
            self.tail = node
        
        else:
            self.tail = self.head = node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Example usage:
linked_list = LinkedList()
linked_list.insert("A")
linked_list.insert("B")
linked_list.insert("C")

print("Linked List:")
linked_list.print_list()
