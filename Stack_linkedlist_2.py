from SLL import*
class stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0

    def is_empty(self):
        return self.mylist.is_empty()

    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1
            

    def peek(self):
        return self.mylist.start.item
    
    def size(self):
        return self.item_count
    
s=stack()
s.push(10)
s.push(2)
s.push(70)
print(s.peek())
print(s.pop())
# print(s.peek())

