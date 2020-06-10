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
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            a = self.storage.pop()
            self.size -= 1
            return a


s = Stack()
s.push(5.8)
s.push(8)
s.push(70)
s.push(598)
s.pop()
print(s.storage)


# With the linked list implementation
class Node:
    def __init__(self, value=None, next_node=None):
        # set the initial value of the node
        self.value = value
        # set a reference to the next node
        self.next_node = next_node

# define a method for getting values, getting the next node, and setting the next node
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# The linked list here


class Linked_list:
    def __init__(self):
        # the initial value will be a reference to head which is the first node in the list
        self.head = None
        # reference to tail of the list
        #self.tail = None

    def add_to_end(self, value):
        # Regardless of if the list is empty or not, we will need a new node.
        new_node = Node(value)
        # We need to think of two edge cases, whether the list is empty or not
        # If the list is empty, we wrap the value in a node and make it the head
        if not self.head:  # If there is no head, our new node becomes the head
            self.head = new_node
        else:  # if there is a head, our new node will be added to the last node on the list. To get to the last node on the list, we need to traverse it.
            current_node = self.head
            while current_node.get_next() is not None:
                current_node = current_node.get_next()
            # At the end of the list,
            current_node.set_next(new_node)

    def remove_from_end(self):
        if not self.head:  # If there is no head
            return None
        else:  # similarly, we need to traverse the list to get to the end
            current_node = self.head
            while current_node.get_next() is not None:
                current_node = current_node.get_next()
            # At the end of the list,
            end_value = current_node.get_value()
            #We remove the value of the last node
            return end_value


class Stack_list:
    def __init__(self):
        self.size = 0
        self.storage = Linked_list()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_end(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            a = self.storage.remove_from_end()
            self.size -= 1
            return a

t = Stack_list()
t.push(99)
print(t.pop())