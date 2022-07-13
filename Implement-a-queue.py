class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.queue = []

    '''----------------- Public Functions of Queue -----------------'''

    def isEmpty(self) :
        #Implement the isEmpty() function
        return len(self.queue)==0

    def enqueue(self, data) :
        #Implement the enqueue(element) function
        self.queue.append(data)

    def dequeue(self) :
        #Implement the dequeue() function
        if self.isEmpty(): return -1
        return self.queue.pop(0)
        
    def front(self) :
        #Implement the front() function
        if self.isEmpty(): return -1
        return self.queue[0]
      
# Time: O(1)
# Space: O(1)
