class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def removeDuplicates(self):
        if not self.head:
            return
        temp1 = self.head

        while temp1:
            prev = temp1
            temp2 = temp1.next
            while temp2:
                if temp1.data == temp2.data:
                    prev.next = temp2.next
                    temp2 = prev.next
                else:
                    prev = prev.next
                    temp2 = temp2.next
            temp1 = temp1.next
        return


    # def sortList(self):
    #     # Node current will point to head
    #     current = self.head
    #
    #     if self.head is None:
    #         return
    #     else:
    #         while current is not None:
    #             # Node index will point to node next to current
    #             index = current.next
    #
    #             while index is not None:
    #                 # If current node's data is greater than index's node data, swap the data between them
    #                 if current.data > index.data:
    #                     temp = current.data
    #                     current.data = index.data
    #                     index.data = temp
    #                 index = index.next
    #             current = current.next

    def disp(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
four = Node(2)
five = Node(3)
ll.head.next = second
second.next = third
third.next = four
four.next = five

ll.disp()
ll.removeDuplicates()
ll.disp()