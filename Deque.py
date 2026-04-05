

class Deque:
    def __init__(self):
        self.q = []

    def length(self):
        return len(self.q)
    
    
    
    def InstartAtStart(self, value):
        self.q.insert(0, value)


   
    def InsertAtEnd(self, value):
        self.q.append(value)


    
    def peekAtTop(self):
        if len(self.q) == 0:
            return f"Empity Stack"                     
        return self.q[0]

    
    
    def peekAtBottom(self):
        ind = len(self.q) - 1
        if len(self.q) == 0:
            return f"Empity Stack"
        return self.q[ind]  # also use -1 for the last index
    

    
    def deleteAtTop(self,):
        if len(self.q) == 0:
            raise Exception("Empity Stack")
        
        self.q.pop(0)


    
    def deleteAtBottom(self,):
        if len(self.q) == 0:
            raise Exception("Empity Stack")
        
        self.q.pop()
        

sta = Deque()

# print(sta.length())
# print(sta.peekAtBottom())
sta.InstartAtStart(3)
sta.InstartAtStart(2)
print(sta.peekAtTop())
sta.InsertAtEnd(1)
print(sta.peekAtBottom())
# print(sta.peekAtTop())
# print(sta.length())
# sta.deleteAtTop()
sta.deleteAtBottom()
print(sta.peekAtBottom())



