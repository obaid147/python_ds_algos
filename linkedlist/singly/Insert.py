class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Time Complexity --> O(1)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Time Complexity --> O(n)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Time Complexity --> O(n)
    def insertAfterIndex(self, index, data):
        global x
        new_node = Node(data)
        temp = self.head
        if not self.head:
            print("EMPTY LINKED-LIST")
            return
        else:
            while temp:
                if x == index:
                    break
                x += 1
                temp = temp.next
            if x == index:
                new_node.next = temp.next
                temp.next = new_node
            else:
                print(index, "Index not found")
                return

    # Time Complexity --> O(1)
    def insertAfter(self, prev_node, data):
        new_node = Node(data)
        if prev_node is None:
            print('prev_node is empty')
            return
        new_node.next = prev_node.next
        prev_node.next = new_node


ll = SinglyLinkedList()
#
x = 0
ll.head = Node(1)
second = Node(2)
third = Node(3)
ll.head.next = second
second.next = third
ll.append(100)
ll.prepend(50)
ll.insertAfter(third, 200)
ll.insertAfterIndex(1, 73)