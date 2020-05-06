class LruStack:
    size = 5
    stack = [] * size

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        print(self.stack[-1])

    def put(self, data):
        if len(self.stack) >= self.size:
            print("Stack is full")
            return
        self.push(data)
        return

    def get(self):
        self.stack.index()
        return self.pop()


lru = LruStack()

lru.put(100)
lru.put(200)
lru.put(300)
lru.put(400)
lru.put(500)
lru.get()
lru.put(100)

print(lru.stack)
