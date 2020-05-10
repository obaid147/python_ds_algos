class Stack:
    def __init__(self):
        self.stack = []
        self.tos = -1

    def push(self, data):
        self.tos += 1
        self.stack.append(None)
        self.stack[self.tos] = data

    def pop(self):
        if self.tos == -1:
            return None
        data = self.stack[self.tos]
        del self.stack[self.tos]
        self.tos -= 1
        return data

    def peek(self):
        if self.tos != -1:
            print(self.stack[self.tos])

    def sizeStack(self):
        return len(self.stack)


stack = Stack()
stack.push('A')
stack.push(2.5)
stack.push(True)
stack.push(55)

print("Len: ", stack.sizeStack())
print("popped ", stack.pop())
print("Len:", stack.sizeStack())
stack.peek()