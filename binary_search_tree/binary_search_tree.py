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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Here, there are 2 possible cases. We can either insert to the left or right.
        # We insert to the left if the value of what we are inserting is less than out self.value which is the root value
        if value <= self.value:
            # Move to the left and check if it is none
            if not self.left:
                # we insert the node here and set the self.left to be our value
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # Otherwise, we do the right case
        else:
            if not self.right:
                # We insert the node here and set the self.right to be our value
                self.right = BSTNode(value)
                # otherwise
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # To know if a binary tree contains a value, we have to check if the target equals the self.value and its left and right elements
        if target == self.value:
            return True
        # left case
        if target < self.value:
            #We first check if there is anything to the left of self.value
            if self.left is None:
                return False
            else:
            #We bring in our contain method to look for it
                self.left.contains(target)
        #Otherwise we do the right case
        if target > self.value:
            #We first check if there is anything to the right of self.value
            if self.right is None:
                return False
            else:
                #We check with our contain method
                self.right.contains(target)

            # Return the maximum value found in the tree

    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
