class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Time Complexity --> O(n);
    def CycleDetectionUsingSet(self):
        set1 = set()
        temp = self.head
        while temp:
            if temp in set1:
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
        while rab.next and rab and tut.next:
            tut = tut.next
            rab = rab.next.next
            if id(tut) == id(rab):
                return True
        return False

    # Time Complexity --> O(n)
    def CycleDetectionTemp(self):
        if not self.head:
            return None
        temp, temp.next = Node(100), None
        while self.head is not None:
            if self.head.next is None:
                return False
            if self.head.next is temp:
                return True
            nextNode = self.head.next
            self.head.next = temp
            self.head = nextNode
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
five.next = third
# print(ll.CycleDetectionUsingSet())
# print(ll.CycleDetectionFlyodAlgo())
print(ll.CycleDetectionTemp())