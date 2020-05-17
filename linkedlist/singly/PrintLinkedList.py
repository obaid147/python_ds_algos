class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 0(n)
    def printList(self):
        temp = self.head
        if not self.head:
            print("Empty list")
        else:
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

    # Recursive
    def printReverse(self, head):
        if head is None:
            return
        self.printReverse(head.next)
        print(head.data)


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
# ll.printList()
ll.printReverse(ll.head)