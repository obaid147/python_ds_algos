class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.isempty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

    def isempty(self):
        if self.head is None:
            return True
        return False

    def peek(self):
        if not self.isempty():
            print(self.head.data)
        else:
            print("Stack Empty")


ll = StackLinkedList()
ll.push(100)
ll.push(200)
ll.push(300)
ll.peek()
print(ll.pop(), 'pop')
ll.peek()
print(ll.pop(), 'pop')
ll.peek()
