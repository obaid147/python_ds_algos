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
        set1 = set()
        temp = self.head
        flag = False
        prev = Node(None)
        while temp:
            if temp in set1:
                flag = True
                break
            else:
                set1.add(temp)
            prev = temp
            temp = temp.next
        if flag:
            prev.next = None
            return True
        else:
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