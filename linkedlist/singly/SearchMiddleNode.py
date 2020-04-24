class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

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
                print('Middle Node = ', temp.data)

            subMethod1(length)


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
