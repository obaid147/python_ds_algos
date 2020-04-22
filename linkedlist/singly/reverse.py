class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Time Complexity --> O(n)
    def reverseLinkedList(self):
        if not self.head:
            return
        prev_Node = None
        current = self.head
        while current:
            next_Node = current.next
            # break link
            current.next = prev_Node
            # new node
            prev_Node = current
            current = next_Node
        self.head = prev_Node


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
ll.head.next = second
second.next = third
ll.reverseLinkedList()