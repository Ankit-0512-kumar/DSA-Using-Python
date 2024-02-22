class Priorityqueue:
    def __init__(self):
        self.items=[]

    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))

    def is_empty(self):
        return len(self.items)==0    

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items(0)[0]
    
    def size(self):
        return len(self.items)
    
# Driver Code
p=Priorityqueue()
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



