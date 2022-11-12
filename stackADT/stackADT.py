class Stack:
    def __init__(self):
        self.stack = []
        
    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        if not self.isEmpty:
            return "--Stack is empty"

        return self.stack
    
    def __repr__(self):
        return str(self.__str__())
    
    def push(self, item):
        self.stack.append(item)
    
    def remove(self, item):
        if self.binarySearch(item):
            self.stack.remove(item)
            
        else:
            return "--Item not found"
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True

        return False

    def binarySearch(self, item):
        low = 0
        high = len(self.stack)
        
        while low <= high:
            mid = ( low + high ) // 2
            if self.stack[mid] == item:
                return True
            
            elif self.stack[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
                
        return False