class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next
        
class SinglyLinkList:
    def __init__(self, head = None):
        self.head = head

    def InsertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp


    def InsertAtMid(self, value, loc):
        temp = Node(value)
        t1 = self.head
        if self.head is None:
            self.head = temp
            return    
        while t1 is not None:
            if t1.data == loc:
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
        print(f"{loc} not found")


    def InsertAtEnd(self,value):
        if self.head is not None:
            temp = Node(value)
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
        
    def printLL(self):
        t1 = self.head
        if t1 is None:
            print("Empity list!")
        while t1 is not None:
                print(t1.data)
                t1 = t1.next


obj = SinglyLinkList()
obj.InsertAtBeg(3)
obj.InsertAtBeg(2)
obj.InsertAtBeg(1)
obj.InsertAtEnd(6)
obj.InsertAtMid(2,2)
obj.InsertAtMid(2,4)
obj.InsertAtEnd(7)

obj.printLL()
