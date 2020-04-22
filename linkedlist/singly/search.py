class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Time Complexity --> O(n)
    # Space Complexity --> O()
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

    def searchByData(self, Data):
        temp = self.head
        if temp is not None:
            if temp.data == Data:
                return True
        while temp is not None:
            if temp.data == Data:
                return True
            temp = temp.next
        if temp is None:
            return
        return False


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
ll.head.next = second
second.next = third
print(ll.searchByData(100))