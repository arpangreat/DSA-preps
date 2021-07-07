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

    def add(self, data):
        """
            Adds New Node containing data at head of the list
            Takes O(1) Time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
            Search for the first node containing the data that matched the key
            Returns the node or `None` if not found

            Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current == current.next_node

            return None

    def insert(self, data, index):
        """
            Inserts A new node containing data in index position
            Insertion takes O(1) time but finding the node at the Insertion points takes O(n) time
            
            i.e. It Takes over-all O(n)
        """

        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.data

            while position > 1:
                current = node.next_node
                position -= 1

            prev = current
            next = current.next_node

            prev.next_node = new
            new.next_node = next

    def remove(self, key):
        """
            Removes node containing the data that matches the key
            Returns the node or None if the key doesn't exists
            Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """
            Returns a String represantation of the list
            Takes O(n) time
        """

        nodes= []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)

            current = current.next_node
        return '-> '.join(nodes)



