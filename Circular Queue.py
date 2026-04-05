class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1  

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
            return
        elif (self.rear == -1 and self.front == -1):
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

    def dequeue(self):
        if (self.front == -1):
            print("Queue is Empty!")
            return
        
        print(f"Dequeued: {self.items[self.front]}")
        
        if self.rear == self.front:
            self.front = self.rear = -1       
        else:
            self.front = (self.front + 1) % self.size



CQ = CircularQueue(5)

CQ.enqueue(1)
CQ.enqueue(2)
CQ.enqueue(3)
CQ.enqueue(4)
CQ.enqueue(5)
CQ.enqueue(6)
CQ.dequeue()
CQ.dequeue()
CQ.dequeue()
CQ.dequeue()
CQ.dequeue()
CQ.dequeue()
CQ.dequeue()
CQ.enqueue(19)
CQ.dequeue()