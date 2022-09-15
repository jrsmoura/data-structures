from unittest import TestCase


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """ Function to insert a new node at the beginning
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    @classmethod
    def insert_after(cls, previous_node, new_data):
        if previous_node is None:
            return "The given previous node must inLinkedList"

        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        temp = self.head
        data = [temp]
        while temp:
            # print(temp.data)
            temp = temp.next
            data.append(temp)
        return data


class TestLinkedList(TestCase):
    def test_push(self):
        llist = LinkedList()
        llist.head = Node(2)
        second = Node(3)
        third = Node(4)
        llist.head.next = second
        second.next = third
        llist.push(1)

        assert llist.print_list() == [1, 2, 3, 4]

    def test_insert_after(self):
        self.fail()

    def test_append(self):
        self.fail()

    def test_print_list(self):
        self.fail()
