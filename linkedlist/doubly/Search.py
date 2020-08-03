class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def searchByData(self, SearchData):
        if not self.head:
            return None

        temp = self.head
        while temp:
            if temp.data == SearchData:
                return temp.data
            else:
                temp = temp.next
        return 'Not Found'

    def searchByIndex(self, index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        if not temp:
            return
        print(self.searchByData(temp.data))


dll = DoublyLinkedList()
dll.head = Node(100)
dll.sec = Node(200)
dll.third = Node(300)
dll.head.next = dll.sec
dll.sec.next = dll.third

print(dll.searchByData(400))
# dll.searchByIndex(2)
