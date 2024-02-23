class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=ite
        self.next=next

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.item_count==0

    def insert_front(self,data):
        n=Node(data,None,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.item_count+=1

    def insert_rear(self,data):
        n=Node(data,self.rear)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.rear.prev=None
        self.item_count-=1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.rear.item

    def size(self):
        return self.item_count

# Driver Code
d2=Deque()
d2.insert_front(10)
d2.insert_front(5)
d2.insert_rear(30)
d2.insert_rear(40)
print(d2.get_front(),d2.get_rear())
# d2.delete_front()
d2.delete_rear()
print(d2.get_front(),d2.get_rear())                   






