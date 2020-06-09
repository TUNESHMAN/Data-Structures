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
            a=self.storage.pop()
            self.size-=1
            return a
s=Stack()
s.push(5.8)
s.push(8)
s.push(70)
s.push(598)
s.pop()
print(s.storage)
          


# With the linked list implementation
class ClassName:
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

    def set_next(self, new_node):
        self.next_node = new_node

# The linked list here


class Linked_stack:
    def __init__(self):
        # the initial value will be a reference to head
        self.head = None
        # reference to tail of the list
        self.tail = None
