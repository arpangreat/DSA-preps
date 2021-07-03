#  Head           Tail
#
#  Singly Linked List
#
#  [1]->[2]->[3]->[4] // Single Way Nodes (->)
#
#  Doubly Linked List
#
#  [1]<->[2]<->[3]<->[4] // Both Way Nodes (<->)

class Node:
    """
        An object for storing a singly node of a linked list
        Model Two attributes - data and linked to the next node in the list
    """

    data = None
    next_node = None

    def  __init__(self, data) :
        self.data = data

    def __repr__(self):
        return "<Node Data: %s>" %self.data

class LinkedList:
    """
        Singly Linked List
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
            Return the number of nodes in the list 
            Takes O(n) time
        """

        current = self.head
        count = 0

        while current: # same as current != None
            count += 1
            current = current.next_node

        return count


