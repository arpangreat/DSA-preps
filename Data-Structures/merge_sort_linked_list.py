from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts A LinkedList in ascending order
    - Recursively divide linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns A Sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges Two LinkedList sorting by data in the nodes
    Returns a new merged list
    """

    # Create a new linked list that contains nodes from
    # merging left and right
    merged = LinkedList()

    # Add a fake head that discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for the left and right
    left_head = left.head
    right_head = right.head

    # Iterating Over left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # If the head node of left linked list None, we pass the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to false
            right_head = right_head.next_node
        # if the head node of the right is None, we pass the tail
        # Add the tail node to left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            # Not at either tail node Obtain node data to perform
            # comparison operation
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current node to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to the next node
                left_head = left_head.next_node
            # If data on left is larger than right, set current node to right node
            else:
                current.next_node = right_head
                # move right head to the next node
                right_head = right_head.next_node

        # Move current to the next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(52)
l.add(12)
l.add(98)
l.add(67)
l.add(8)
l.add(78)
print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
