class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Time Complexity --> O(n)
    def searchByIndex(self, data_index):
        if not self.head:
            return
        temp = self.head
        i = 0
        while temp:
            if data_index == i:
                print("Data at index", data_index, "is", temp.data)
                return
            if temp.next is None:
                return
            temp = temp.next
            i += 1


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
ll.head.next = second
second.next = third