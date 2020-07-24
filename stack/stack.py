import sys
sys.path.append('..')
from singly_linked_list.singly_linked_list import LinkedList  # pylint: disable=global-statement

""" 
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        return self.storage.pop()


# test_arr = [3, 4, 6, 4, 5, 6]
# arr_stack = Stack(test_arr)
# print(arr_stack)
# list_stack = LinkedList()
# ourStack = Stack(list_stack)
# print(ourStack.__len__())
# ourStack.push(7)
# print(ourStack.__len__())
# ourStack.pop()
# print(ourStack.__len__())
