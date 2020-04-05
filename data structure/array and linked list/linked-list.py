# Types of Linked Lists
# In this notebook we'll explore three versions of linked-lists: singly-linked lists, doubly-linked lists, and circular lists.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# A small linked list:

head = Node(1)
head.next = Node(2)