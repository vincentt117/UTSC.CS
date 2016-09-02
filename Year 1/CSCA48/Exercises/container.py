class ContainerFullException(Exception):
    pass
class ContainerEmptyException(Exception):
    pass

class ContainerQueue():
    def __init__(self):
            self._content = []
        
    def put(self, item):
        self._content.append(item)
        
    def get(self):
        if self.is_empty():
            raise ContainerEmptyException
        ret_item = self._content.pop(0)
        return ret_item
            
    def is_empty(self):
        return self._content == []  
                
    def peek(self):
        if self.is_empty():
            raise ContainerEmptyException        
        return self._content[0]
    
    def copy(self):
        c = ContainerQueue()
        c._content = self._content[:]
        return c

class ContainerBucket(ContainerQueue):
    
    def put(self, item):
        if self.is_full():
            raise ContainerFullException
        self._content.append(item)
    
    def is_full(self):
        return self._content != []
    
    def copy(self):
        c = ContainerBucket()
        c._content = self._content[:]
        return c    
    
class ContainerStack(ContainerQueue):
        
    def get(self):
        if self.is_empty():
            raise ContainerEmptyException
        ret_item = self._content.pop()
        return ret_item 
                
    def peek(self):
        if self.is_empty():
            raise ContainerEmptyException        
        return self._content[-1]
    
    def copy(self):
        c = ContainerStack()
        c._content = self._content[:]
        return c    
    


            
        
    
        
        
        