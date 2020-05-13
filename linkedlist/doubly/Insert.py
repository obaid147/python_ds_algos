class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        newNode = Node(data)

        newNode.next = temp
        temp.prv = newNode
        self.head = newNode

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        newNode = Node(data)
        while temp.next is not None:
            temp = temp.next
        newNode.prev = temp
        temp.next = newNode

    def insertAfterNode(self, prev_node, new_data):
        if not prev_node:
            return

        new_node = Node(data=new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


dll = DoublyLinkedList()

dll.head = Node(100)
dll.sec = Node(200)
dll.head.next = dll.sec
dll.insertAfterNode(dll.head, 12)
dll.print()

