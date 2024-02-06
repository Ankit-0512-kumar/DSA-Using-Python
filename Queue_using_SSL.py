class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front==None

    def enqueue(self,data):
        n= Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is Empty')
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError('no data in queue')
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError('no data in queue')
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count

# Driver Code
q2=Queue()
q2.enqueue(10)
q2.enqueue(15)
q2.enqueue(20)
print('front item is =',q2.get_front())   
print('Rear item is =',q2.get_rear())
print("size =",q2.size())
q2.dequeue()
print('front item is =',q2.get_front())   
print('Rear item is =',q2.get_rear())
print("size =",q2.size())

