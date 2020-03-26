# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')

# from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next


    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev


    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # TODO: Catch errors if list is empty or node is not in list
        # For now assumine node is in list
        self.length -= 1
        # if head and tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # if head
        elif node is self.head:
            self.head = self.head.next
            node.delete()

        # if tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            # if regular node
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        # Loop through all nodes, looking for biggest value
        # TODO: Error checking
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value

class Queue:
    def __init__(self):
        # counter to keep track of the number of elements in our queue
        self.size = 0
        # we'll use our LinkedList implementation to build the queue
        self.storage = DoublyLinkedList()
    def enqueue(self, item):
        # add the item to the linked list
        self.storage.add_to_tail(item)
        # increment our size counter
        self.size += 1
    def dequeue(self):
        # decrement our size counter
        if self.size > 0:
            self.size -= 1
            # remove the head of the linked list and return it
            return self.storage.remove_from_head()
        else:
            return None
    def len(self):
        return self.size


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new = BinarySearchTree(value)
        if not self.value:
            return new
        if value < self.value:
            if not self.left:
                self.left = new
            else:
                # recursion (do same thing with that left node)
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new
            else:
                # recursion (do same thing with that right node)
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if not self.value:
            return False
        if target == self.value:
            return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return None
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if not self.value:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb) 

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.len() > 0:
            popped_node = q.dequeue()
            print(popped_node.value)
            if popped_node.left:
                q.enqueue(popped_node.left)
            if popped_node.right:
                q.enqueue(popped_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.size > 0:
            popped_node = s.pop()
            print(popped_node.value)
            if popped_node.left:
                s.push(popped_node.left)
            if popped_node.right:
                s.push(popped_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
