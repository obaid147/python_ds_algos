# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # O(n*d)
    def CycleDetectionUsingSet(self):
        set1 = set()
        temp = self.head
        while temp:
            if temp.next in set1:
                return True
            else:
                set1.add(temp)
            temp = temp.next
        return False

    # O(n)
    def CycleDetectionFlyodAlgo(self):
        if not self.head:
            return None
        tut = self.head
        rab = self.head
        while rab.next is not None and rab is not None or tut is not None:
            tut = tut.next
            rab = rab.next.next
            if id(tut) == id(rab):
                return True
        return False

    # O(1)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # O(n)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

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

    def insertAfter(self, prev_node, data):
        new_node = Node(data)
        if prev_node is None:
            print('prev_node is empty')
            return
        new_node.next = prev_node.next
        prev_node.next = new_node
# ---------------------------------NEW METHODS-------------------------------------------------------------

    def delFirst(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
            return
        else:
            self.head = self.head.next
            return

    def deleteNode(self, key):
        temp = self.head
        prev = None
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def SearchByIndex(self, data_index):
        if not self.head:
            return
        temp = self.head
        i = 0
        while temp:
            if data_index == i:
                print("Data at index", data_index, "is", temp.data)
                return
            if temp.next is None:
                return
            temp = temp.next
            i += 1

    def reverseLinkedList(self):
        if not self.head:
            return
        prev_Node = None
        current = self.head
        while current:
            next_Node = current.next
            # break link
            current.next = prev_Node
            # new node
            prev_Node = current
            current = next_Node
        self.head = prev_Node

# -----------------------------------------------------------------------------------------------
    # O(n)
    def length_iterative(self):
        global global_length
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print('length = ', count)
        global_length = count

    # 0(n)
    def printList(self):
        temp = self.head
        if not self.head:
            print("Empty list")
        else:
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

    def deleteLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        temp = self.head
        while temp.next.next:  # while (third node) as first two NODES are already handled
            temp = temp.next
        temp.next = None
        return

    def delete_index(self, index):
        if self.head is None:
            return
        temp = self.head

        if index == 0:  # index zero is handled here
            self.head = temp.next
            temp.next = None
            return

# if index is 1 loop will not execute as the range is index - 1 ==> zero
# if index is 2 then the loop will iterate only once index - 1 ==>1 ie: 0 to 1 excluding 1

        for i in range(index - 1):
            temp = temp.next
            if temp is None:  # if length of linkedlist is less than the loop iterations then break
                break

# If break then this
# This checks the Node before index_Node
        if temp is None:
            return

        # Error is if index is one > than the size of linked-list
# This checks the index_NODE itself
        if temp.next is None:
            return

# This next will store the reference of the Node which comes after index_NODE if available
        next = temp.next.next

# temp.next is the node itself which will point to None...
        temp.next = None

# As 'temp' is the node before Index_NODE
# temp will store the reference of 'next' as next variable is the reference of the Node that was after our Index_NODE
        temp.next = next


# Code execution starts here
# Start with the empty list
ll = SinglyLinkedList()
#
x = 0
global_length = 0
ll.head = Node(1)
second = Node(2)
third = Node(3)
four = Node(4)
five = Node(5)
ll.head.next = second
second.next = third
third.next = four
four.next = five
five.next = ll.head
# ll.printList()
# print()
# ll.delete_index(6)
# # ll.delFirst()
# ll.deleteNode(6)
# ll.printList()
# print()
# ll.SearchByIndex(6)

# ll.reverseLinkedList()
# ll.printList()
# delfirst
# delByData
print()

print(ll.CycleDetectionUsingSet())
print(ll.CycleDetectionFlyodAlgo())