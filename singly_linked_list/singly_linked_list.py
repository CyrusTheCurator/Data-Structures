# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

# A Linked List class with a single head node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if(self.head is None and self.tail is None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if(self.head is None and self.tail is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def insert(self, value):
        newNode = Node(value)
        if(self.head):
            current = self.head
            while(current.next_node):
                current = current.next_node
            current.next_node = newNode
        else:
            self.head = newNode

    def remove_head(self):
        # If list is empty, do nothing
        if not self.head:
            return None
        # if list has one element, set head and tail to none
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # with more than one element in list, Do:
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def printLL(self):
        current = self.head
        while(current):

            print(current.value)
            current = current.next_node

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None

        current_node = self.head
        list_max = 0
        while current_node is not None:
            if current_node.value > list_max:
                list_max = current_node.value
            current_node = current_node.next_node
        return list_max


LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
