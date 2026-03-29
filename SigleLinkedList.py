class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def InsertAtEnd(self, value):
        temp = Node(value)
        
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
            
    def PrintLL(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)
        
obj = SinglyLinkedList()
obj.InsertAtEnd(5)
obj.InsertAtEnd(6)
obj.InsertAtEnd(7)
obj.PrintLL()