class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def Enqueue(self, data):
        newNode = Node(data)

        if self.rear is None:
            self.front = self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def Dequeue(self):
        if self.front is None:
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None

    def printFront(self):
        if not self.front:
            return 'Empty'
        else:
            return self.front.data


if __name__ == '__main__':
    qll = QueueLinkedList()
    qll.Enqueue(100)
    qll.Enqueue(200)
    qll.Enqueue(300)
    qll.Enqueue(400)
    qll.Enqueue(500)
    print("Front --->", qll.printFront())
    qll.Dequeue()
    qll.Dequeue()
    qll.Dequeue()
    print("--> After DeQueue <--")
    print("Front --->", qll.printFront())