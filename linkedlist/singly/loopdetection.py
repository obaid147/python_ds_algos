class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Time Complexity --> O(n*d);
    def CycleDetectionUsingSet(self):
        set1 = set()
        temp = self.head
        while temp:
            if temp.next in set1:
                return True
            else:
                set1.add(temp)
            temp = temp.next
        return False

    # Time Complexity --> O(n)
    def CycleDetectionFlyodAlgo(self):
        if not self.head:
            return None
        tut = self.head
        rab = self.head
        while rab.next is not None and rab is not None or tut is not None:
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
five.next = None
print(ll.CycleDetectionUsingSet())
print(ll.CycleDetectionFlyodAlgo())