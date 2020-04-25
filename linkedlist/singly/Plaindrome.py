class Stack:
    stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        print(self.stack[-1])


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def compare(self):
        if not self.head:
            return
        stk = Stack()
        temp = self.head
        while temp:
            stk.push(temp.data)
            temp = temp.next
        temp = self.head

        while temp.next:
            if stk.pop() != temp.data:
                return 'Not Palindrome'
            else:
                temp = temp.next
        if temp.next is None:
            return 'Palindrome'
        else:
            return 'None Palindrome'


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(5)
third = Node(5)
four = Node(5)
five = Node(1)
ll.head.next = second
second.next = third
third.next = four
four.next = five

print(ll.compare())
