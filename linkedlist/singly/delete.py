class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Time Complexity --> O(n)
    # Space Complexity --> O()
    def deleteLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return

    # Time Complexity --> O(n)
    # Space Complexity --> O()
    def delete_index(self, index):
        if self.head is None:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            temp.next = None
            return
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    # Time Complexity --> O(1)
    # Space Complexity --> O()
    def delFirst(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
            return
        else:
            self.head = self.head.next
            return

    # Time Complexity --> O(n)
    # Space Complexity --> O()
    def deleteNode(self, key):
        temp = self.head
        prev = None
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
four = Node(4)
five = Node(5)
ll.head.next = second
second.next = third
third.next = four
four.next = five
ll.deleteLast()
ll.delete_index(0)
ll.delFirst()
ll.deleteNode(5)