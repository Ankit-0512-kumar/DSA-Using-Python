class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def nqueue(self,data):
        self.items.append(data)

    def dqueue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")

    def size(self):
        return len(self.items)

# Driver code 
q1=Queue()
q1.nqueue(10)
q1.nqueue(12)
q1.nqueue(15)
q1.nqueue(20)
print("rear value is ",q1.get_rear())
print("front value is ",q1.get_front())
q1.dqueue()   
print("front value is ",q1.get_front()) 
# print("rear value is ",q1.get_rear()) 
print("size=",q1.size())      
# q1.dqueue()     
# print("size=",q1.size())  

