class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None



ll = DoublyLinkedList()
ll.head = Node(1)
sec = Node(2)
three = Node(3)
four = Node(2)
five = Node(1)

ll.head.next = sec
sec.next = three
three.next = four
four.next = five

print(ll.funPalindrome(ll.head))