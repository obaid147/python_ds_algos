class Queue:
    def __init__(self):
        self.que = []
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.front == -1:
            return True
        else:
            return False

    def push(self, data):
        self.que.append(None)
        self.front += 1
        self.rear += 1
        self.que[self.front] = data

    def pop(self):
        if self.isEmpty():
            return None
        else:
            x = self.que.pop(self.rear)
            self.front -= 1
            self.rear -= 1
            return x