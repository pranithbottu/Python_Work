"""
Homework 5 - Linked Lists

Release Date: 10-24
Due Date: 10-31 : s p o o k y :

To understand recursion, you must first understand recursion.
"""

class Node(object):
    """
    Class for linked list node.
    """
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node


	def add_head(head, data):
    """
    Given the head of a linked list, appends the given element to
    the head.

    Input:
        head - the head of the linked list.
        data - the item to add to the head of the linked list.
    
    Output:
        the newly created linked list.
    """
		head.next_node = data
		return head

	def add_position(head, data, position):
    """
    Given the head of a linked list, adds a new element so that
    it is at the given position. If the position is greater than
    the length of the linked list, place the new element at the end
    of the linked list.

    Input:
        head - the head of the linked list.
        data - the item to add to the linked list.
        position - the position to add the element in the linked list.
    
    Output:
        the head of the linked list.
    """
		start = head
		if position == 0:
			return Node(data, head)
		while position > 1:
			head = head.next_node
			position -= 1
		head.next_node = Node(data, head.next_node)
		return start

	def remove_head(head):
    """
    Given the head of a linked list, removes the first element.
    If head is None, returns None.

    Input:
        head - the head of the linked list.
    
    Output:
        the new head of the linked list.
    """
		if head != None:
			head = head.next_node
			return head
		else:
			return None

	def remove_position(head, position):
    """
    Given the head of a linked list, removes the element of the 
    specified position. If the position is greater than the length
    of the linked list, do not remove anything.

    Input:
        head - the head of the linked list.
        position - the position at which to remove an element.
    
    Output:
        the head of the linked list.
    """
		count = 0
		start = head
		while head.next_node != None:
			count+=1
		if position > count:
			return head
		else:
			while position > 1:
				head = head.next_node
				position -= 1
			head.next_node = Node(head, head.next_node)
		return start

	def list_sum(head):
    """
    Given the head of a linked list with integer elements, returns
    the sum of the linked list.

    Input:
        head - the head of the linked list.
    
    Output:
        (int) the sum of the elements in the linked list.
    """
		sum = 0
		while head != None:
			sum += head.data
			head = head.next_node
		return sum

	def is_merged(head_a, head_b):
    """
    Given the heads of two linked lists, determines if the linked
    lists merge at some point.

    Input:
        head_a - the head of the first linked list.
        head_b - the head of the second linked list.
    
    Output:
        (bool) whether or not the linked lists merge.
    """
		dont_merge = True
		while dont_merge & (head_a != None):
			while dont_merge & (head_b != None):
				if head_a != head_b:
					head_b = head_b.next_node
				elif head_a == head_b:
					return True
			head_a = head_a.next_node
		return False

	def find_merge_point(head_a, head_b):
    """
    Given the heads of two linked lists that merge, returns the
    data at that merge point.
    
    This will only be called on lists where
    is_merged(head_a, head_b) is true.

    Input:
        head_a - the head of the first linked list.
        head_b - the head of the second linked list.
    
    Output:
        the element at the merge point.
    """
		dont_merge = True
		while dont_merge & (head_a != None):
    			while dont_merge & (head_b != None):
				if head_a != head_b:
					head_b = head_b.next_node
				elif head_a == head_b:
					return head_b.data
			head_a = head_a.next_node

	def find_cycle(head):
    """
    Given the head of a linked list, determines whether or not there
    is a cycle in the linked list.

    Input:
        head - the head of the linked list.
    
    Output:
        (bool) whether or not there is a cycle in the linked list.
    """
    		pass
