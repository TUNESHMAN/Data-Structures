"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        a = self.storage.insert(0, value)
        self.size += 1
        return a

    def dequeue(self):
        if self.size > 0:
            b = self.storage.pop()
            self.size -= 0
            return b


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
print(q.storage)

# With linked list


class Queue:
    def __init__(self, value=None, next_node=None):
        # Here, we set the initial value of the node
        self.value = value
        self.next_node = next_node

# Define methods for getting values, getting next node, and setting the next node.

    def get_values(self, value):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# The linked list here


class Linked_stack:
    def __init__(self):
        # the initial value will be a reference to head which is the first node in the list
        self.head = None
        # reference to tail of the list
        #self.tail = None

    def add_to_end(self, value):
        # Regardless of if the list is empty or not, we will need a new node.
        new_node = Queue(value)
        # We need to think of two edge cases, whether the list is empty or not
        # If the list is empty, we wrap the value in a node and make it the head
        if not self.head:  # If there is no head, our new node becomes the head
            self.head = new_node
        else:  # if there is a head, our new node will be added to the last node on the list. To get to the last node on the list, we need to traverse it.
            current_node = self.head
            while current_node.get_next() is not None:
                current = current_node.get_next()
            # At the end of the list,
            current.set_next(new_node)

    def remove_from_start(self):
        if not self.head:  # If there is no head
            return None
        else:  # Here, we are concerned about removing the first element which is the head element
            current_node = self.head
            while current_node.get_next() is not None:
                # At the end of the list,
                start_value = current_node.get_value()
            # We remove the value of the last node
            return start_value
