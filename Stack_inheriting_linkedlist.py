from SLL import*
class Stack(SLL):
    def __init__(self):
        super().__init__()
        # this super for call prante class _init_ method 
        self.item_count=0
        # this function for size count ortherwise we done this code without __init__method

    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        return self.item_count 
    
# driver code
s2=Stack()
s2.push(10)
s2.push(20)
s2.push(25)
print("top element is",s2.peek())
s2.pop()
print("pop element is",s2.peek())        

        