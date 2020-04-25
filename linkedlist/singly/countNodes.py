class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # iterative
    def method1(self):
        count = 0
        while self.head:
            count = count + 1
            self.head = self.head.next
        return count

    # recursive
    def method2(self, node):
        if not node:
            return 0
        else:
            return 1 + self.method2(node.next)


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
ll.head.next = second
second.next = third
print(ll.method2(ll.head))
print(ll.method1())
