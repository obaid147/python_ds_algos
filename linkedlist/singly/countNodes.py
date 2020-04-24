class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # recursive
    def countNodes(self, node):
        if not node:
            return 0
        else:
            return 1 + self.countNodes(node.next)


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
ll.head.next = second
second.next = third
ll.countNodes(ll.head)
