class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # TC-->O(n) sc-->O(1)
    def method1(self):
        if not self.head:
            return
        else:
            temp = self.head
            length = 0
            while temp:
                length += 1
                temp = temp.next

            def subMethod1(len):
                temp = self.head
                for i in range(len//2):
                    temp = temp.next
                print(temp.data)
            subMethod1(length)

    # TC-->O(n) sc-->O(1)
    def method2(self):
        if not self.head:
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    # TC-->O(n) sc-->O(1)
    def method3(self):
        if not self.head:
            return
        index = 0
        temp = self.head
        mid_Node = self.head
        while temp:
            if index & 1 == 1:
                mid_Node = mid_Node.next
            index += 1
            temp = temp.next
        print(mid_Node.data)


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
ll.head.next = second
second.next = third
third.next = four
four.next = five
five.next = six
ll.method1()
ll.method2()
ll.method3()
