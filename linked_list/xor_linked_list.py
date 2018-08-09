'''
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
'''

# TODO: store size of the linked list to make get operation faster

class XORLinkedList:

    class XORLinkedListNode:

        def __init__(self, value):
            self.both = 0 # XOR of prev and next node memory address
            self.value = value
        
    def __init__(self):
        self.head = None # head XORLinkedListNode object
        self.tail = None # tail XORLinkedListNode object

    def get_pointer(self, node):
        # Given a node, returns the memory address of the node
        # Assumes that this method works correctly
        return None

    def dereference_pointer(self, address):
        # Given an address, returns the node at the address
        # Assumes that this method works correctly
        return None

    def add(self, element):
        node = self.XORLinkedListNode(element)
        if self.tail is None:
            self.head, self.tail = node, node
        else:
            self.tail.both ^= self.get_pointer(node)
            node.both = self.get_pointer(self.tail)
            self.tail = node

    def get(self, index):
        if index == 0 or self.head == None:
            return self.head
        node = self.head
        nextNode = self.dereference_pointer(node.both)
        while (index > 0):
            # store nextNode address before jumping
            nextNodeAddress = self.get_pointer(nextNode)
            # jump nextNode to next
            nextNode = self.dereference_pointer(nextNode.both ^ self.get_pointer(node))
            # jump node to next
            node = self.dereference_pointer(nextNodeAddress)
        return node