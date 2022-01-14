from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif self.head.value >= value:
            new_node.next = self.head
            self.head = new_node