from Node import Node


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
        else:
            runner = self.head.next
            previous = self.head

            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next

            new_node.next = runner
            previous.next = new_node

    def print_list_items(self):
        if self.head is None:
            print("Empty")
        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end=" ")
                runner = runner.next
            print() 

    def count_nodes(self):
        count = 0
        runner = self.head

        while runner is not None:
            count += 1
            runner = runner.next

        return count

    def find_node(self, target_val):
        runner = self.head
        while runner is not None:
            if runner.value == target_val:
                return True
            runner = runner.next
        return False

    def delete_node(self, target_val):
        if self.head is None:
            return False
        elif self.head.value == target_val:
            self.head = self.head.next
            return True