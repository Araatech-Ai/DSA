class Queue():
    def __init__(self):
        self.q = []

    def add(self, value):
        self.q.append(value)

    def delete(self):
        if not self.q:
            return f"Empity Queue"
        return self.q.pop(0)
    
    def peek(self):
        if not self.q:
            return f"Empity Queue"
        return self.q[0]
        
    def lenght(self):
        if not self.q:
            return f"Empity Queue"
        return len(self.q)
    
Q = Queue()
print(Q.delete())
print(Q.peek())
print(Q.lenght())
Q.add(1)
Q.add(2)
Q.add(3)
print(Q.delete())
print(Q.peek())
print(Q.lenght())