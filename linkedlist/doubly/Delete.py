class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def deleteNode(self, myNode):
        if not self.head or myNode:
            return
        if not self.head.next:
            return

        if self.head == myNode:
            self.head = myNode.next
            return

        if myNode.next is not None:
            myNode.next.prev = myNode.prev

        if myNode.prev is not None:
            myNode.prev.next = myNode.next

    def deleteByIndex(self, index):
        i = -1
        temp = self.head
        while temp:
            i += 1
            temp = temp.next

        if not self.head:
            return
        # if not self.head.next:
        #     return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head.next
        for x in range(1, i):
            if index == x:
                if temp.next is not None:
                    temp.next.prev = temp.prev

                if temp.prev is not None:
                    temp.prev.next = temp.next




    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


dll = DoublyLinkedList()
dll.head = Node(100)
dll.sec = Node(200)
dll.third = Node(300)
dll.head.next = dll.sec
dll.sec.next = dll.third

dll.print()
dll.deleteByIndex(0)
print("========================================================================")
dll.print()