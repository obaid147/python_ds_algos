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
        self.second_half = Node(None)

    # TC -> O(n) aux-> O(n)
    def method1(self):
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

    def method2(self):
        if not self.head:
            return False
        if not self.head.next:
            return False

        fast = self.head
        slow = self.head
        prev_slow = None  # 2
        previous = None
        mid = None

        while slow and fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        prev_slow.next = None

        if fast:  # if fast not null then odd ll else even ll
            mid = slow
            slow = slow.next

        self.second_half = slow
        prev_slow.next = None

        self.reverse()
        isPalindrome = self.compare(self.head, self.second_half)
        self.reverse()

        if mid:
            prev_slow.next = mid
            mid.next = self.second_half
        else:
            prev_slow.next = self.second_half

        return isPalindrome

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        current = self.second_half
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        c = previous
        self.second_half = previous

    def compare(self, temp1, temp2):
        while temp1 is not None and temp2 is not None:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        if temp1 is None and temp2 is None:
            return True
        return False


ll = SinglyLinkedList()
ll.head = Node(1)
second = Node(2)

ll.head.next = second

print(ll.method2())
# ll.print()
