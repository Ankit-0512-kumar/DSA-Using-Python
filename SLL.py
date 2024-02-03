#################        ''' Singly Link list '''

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self,start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n=Node(data, self.start)
        self.start = n
        
    def insert_at_last(self, data):
        n=Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next 
        return None           

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_start(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, Data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == Data:
                self.start = None
        else:
            temp = self.start
            if temp.item == Data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == Data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next                            

    def __iter__(self):
        return SLLIterator(self.start)                

class SLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data    
"""
# Driver code
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_at_last(35)
mylist.insert_at_last(40)
mylist.insert_at_last(44)
mylist.insert_after(mylist.search(38), 39)
mylist.insert_after(mylist.search(20), 22)

# Delete the item in list
# mylist.delete_item(44)
# mylist.delete_item(38)
# for x in mylist:
#     print(x, end=' ')

mylist.print_list()            
"""
            

             






        
