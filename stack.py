

class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    
    # 1st Method
    # def push(self, value):
    #     self.s.insert(0, value)


    # 2nd Mathod
    def push(self, value):
        self.s.append(value)


    # 1st Method
    # def peek(self):
    #     if len(self.s) == 0:
    #         return f"Empity Stack"                     
    #     return self.s[0]

    
    # 2nd Mathod
    def peek(self):
        ind = len(self.s) - 1
        if len(self.s) == 0:
            return f"Empity Stack"
        return self.s[ind]  # also use -1 for the last index
    

    # 1st Method
    # def delete(self,):
    #     if len(self.s) == 0:
    #         raise Exception("Empity Stack")
        
    #     self.s.pop(0)


    # 2nd Mathod
    def delete(self,):
        if len(self.s) == 0:
            raise Exception("Empity Stack")
        
        self.s.pop()
        

sta = Stack()

print(sta.length())
print(sta.peek())
sta.push(3)
sta.push(2)
sta.push(1)
print(sta.peek())
print(sta.length())
sta.delete()
print(sta.peek())



