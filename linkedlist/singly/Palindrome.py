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

    def addIntoStack(self):
        stk = Stack()
        temp1 = ll.head
        while temp1:
            stk.push(temp1.data)
            temp1 = temp1.next

    # TC -> O(n) aux-> O(n)
    def method1(self):
        if not self.head:
            return
        self.addIntoStack()
        temp = self.head
        stk = Stack()
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

    # recursive
    def method3(self, temp2):
        stk = Stack()
        if temp2 is None:
            return 'Palindrome'
        else:
            if stk.pop() != temp2.data:
                return 'Not Palindrome'
            else:
                return self.method3(temp2.next)


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
two = Node(2)
three = Node(322)
four = Node(2)
five = Node(1)

ll.head.next = two
two.next = three
three.next = four
four.next = five

# print(ll.method2())

ll.addIntoStack()
print(ll.method3(ll.head))

# ll.print()