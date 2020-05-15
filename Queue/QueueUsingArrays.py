class Queue:
    def __init__(self, c):
        self.front = self.rear = 0
        self.capacity = c
        self.que = [0, 0, 0, 0] * self.capacity

    def queueEnqueue(self, data):
        if self.capacity == self.rear:
            print("\nQueue is full\n")
            return
        else:
            self.que[self.rear] = data
            self.rear += 1
        return

    def queueDequeue(self):
        if self.front == self.rear:
            print("\nQueue is empty\n")
            return
        else:
            for i in range(self.rear - 1):
                self.que[i] = self.que[i + 1]

            if self.rear < self.capacity:
                self.que[self.rear] = 0
                self.rear -= 1
        return

    # // print front of queue
    def queueFront(self):
        if self.front == self.rear:
            print("\nQueue is Empty\n")
            return

        print("\nFront Element is: {}".format(self.que[self.front]))
        return


if __name__ == '__main__':
    q = Queue(4)
    q.queueEnqueue(20)
    q.queueEnqueue(30)
    q.queueEnqueue(40)
    q.queueEnqueue(50)

    # // insert element in the queue
    # q.queueEnqueue(60)

    q.queueDequeue()
    q.queueDequeue()
    print("after two node deletion")

    # // print front of the queue
    q.queueFront()