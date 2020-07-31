"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('..')
from queues.queue import Queue
from stack.stack import Stack



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:

            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not



    def contains(self, target):

        if target is self.value:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()
    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

        return

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):  # removed node param
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)

        while len(queue):
            dequeued_node = queue.dequeue()
            print(dequeued_node.value)
            if dequeued_node.left:
                queue.enqueue(dequeued_node.left)

            if dequeued_node.right:
                queue.enqueue(dequeued_node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)

        while len(stack):
            popped_node = stack.pop()
            print(popped_node.value)
            if popped_node.right:
                stack.push(popped_node.right)
            if popped_node.left:
                stack.push(popped_node.left)
 

        # Stretch Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        self.dft_print(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if self.left:
            self.left.post_order_dft(self.left)

        if self.right:
            self.right.post_order_dft(self.right)
        print(self.value)



"""
This code is necessary for testing the `print` methods
"""


bst = BSTNode(1)

bst.left = BSTNode(2)
bst.right = BSTNode(3)
bst.left.left = BSTNode(4)
bst.left.right = BSTNode(5)



print(f"------------------------------PRE ORDER TRAVERSAL------------------------")
bst.pre_order_dft(bst)
print(f"------------------------------IN ORDER TRAVERSAL------------------------")
bst.in_order_print(bst)
print(f"------------------------------POST ORDER TRAVERSAL------------------------")
bst.post_order_dft(bst)

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
