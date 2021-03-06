class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # TC---->O(n)
    def sizeof(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print('Size of Linked List = ', count)


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
ll.sizeof()
