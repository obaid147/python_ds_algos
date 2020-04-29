class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def BreakCycleDetection(self):
        if not self.head:
            return None
        tut = self.head
        rab = self.head
        while rab.next and rab and tut.next:
            tut = tut.next
            rab = rab.next.next
            if id(tut) == id(rab):
                return True
        return False


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
five.next = second
print(ll.BreakCycleDetection())