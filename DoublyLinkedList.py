class Node:
    def __init__(self, info, prev = None, next = None):
        self.prev = prev
        self.data = info
        self.next = next

class DoublyLinkedList():
    def __init__(self, head = None):
        self.head = head

    def InsertAtBeg(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        temp.next = self.head   
        self.head.prev = temp
        self.head = temp

    def InsertAtMid(self, value, loc):
        temp = Node(value)
        t1 = self.head
        if(self.head is None):
            self.head = temp
            return
        else:
            while(t1 is not None and t1.data != loc):                   
                t1 = t1.next
            if t1 is None:
                print("Locatio is not found!")
                return
            temp.next = t1.next
            if t1.next is not None:
                t1.next.prev = temp
            t1.next = temp
            temp.prev = t1


    def InsertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t1 = self.head
        while(t1.next is not None):
            t1 = t1.next
        t1.next = temp
        temp.prev = t1

    def delNodeDll(self, loc):
        if self.head is None:
            print("Empity list")
            return
        
        t1 = self.head
        if t1.data == loc:
            self.head = t1.next
            self.head.prev = None
            return
        
        while(t1 is not None and t1.data != loc):
            t1 = t1.next
        if t1 is None:
            print(f"Node {loc} is not found")
            return
        
        if t1.next is None and t1.data == loc:
            t1.prev.next = None

        t1.prev.next = t1.next
        t1.next.prev = t1.prev
        
        
        
    def printDLL(self):
        if self.head is None:
            print("Empity list")
            return
        t1 = self.head
        while(t1 is not None):
            print (t1.data)
            t1 = t1.next 
        # print(t1.data)


obj = DoublyLinkedList()
obj.InsertAtBeg(3)
obj.InsertAtBeg(2)
obj.InsertAtBeg(1)
obj.InsertAtMid(4, 2)
obj.InsertAtEnd(4)
obj.InsertAtMid(4, 10)
obj.delNodeDll(3)
obj.printDLL()