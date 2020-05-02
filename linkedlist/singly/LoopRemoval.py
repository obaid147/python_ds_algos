class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def length(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count

    def usingHashing(self):
        if not self.head:
            return None

        set1 = set()
        temp = self.head
        prev = Node(None)
        while temp:
            if temp in set1:
                prev.next = None
                break
            else:
                set1.add(temp)
            prev = temp
            temp = temp.next

    def removeLoopUsingFloydAlgorithm(self):
        if not self.head:
            return None
        tut = self.head
        rab = self.head
        while rab.next and rab and tut.next:
            tut = tut.next
            rab = rab.next.next
            if id(tut) == id(rab):
                # self.removeLoopUsingFloydsAlgo1(self.head, tut)
                print("removing loop with length ", self.length())
                self.removeLoop2(self.head, tut)

    def removeLoop1(self, head, loop):
        ptr1 = head
        while 1:
            ptr2 = loop
            while ptr2 != loop and ptr2.next != ptr1:
                ptr2 = ptr2.next
            if ptr2.next == ptr1:
                break
            ptr1 = ptr1.next
        ptr2.next = None

    def removeLoop2(self, ptr1, ptr2):
        while ptr2.next != ptr1.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        ptr2.next = None


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
# ll.method1()
# ll.method2()
# ll.method3()
ll.removeLoopUsingFloydAlgorithm()
ll.print()