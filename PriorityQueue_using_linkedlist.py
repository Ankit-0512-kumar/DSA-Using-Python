class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self):
        self.item_count=0
        self.start=None

    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority <self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1    

    def is_empty(self): 
        return self.item_count==0

    def pop(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data
    
    def size(self):
        return self.item_count
    
# Drivers code
p=PriorityQueue()
p.push('ankit',2)        
p.push('ram',4) 
p.push('kumar',3) 
p.push('rock',5) 
p.push('amit',6) 
p.push('suman',7) 
p.push('sttr',8) 
p.push('verma',9) 
p.push('shaym',11) 

while not p.is_empty():
    print(p.pop())






