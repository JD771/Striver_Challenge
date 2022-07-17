class node:
    def __init__(self,key= 0, val= 0, prev= None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
        
class LRUCache:

    def __init__(self, capacity: int):
        # dictionary & DLL
        self.head = node()
        self.tail = node()
        self.cache = dict()
        self.capacity = capacity
        self.tail.prev = self.head
        self.head.next = self.tail
        
    def del_(self, key: int)-> int:
        n = self.cache.pop(key)
        n.prev.next = n.next
        n.next.prev = n.prev
        return n.val

    def insert(self, key: int, val: int)-> None:
        n = node(key, val, self.tail.prev, self.tail)
        self.tail.prev.next = self.tail.prev = n
        self.cache[key] = n
        
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        val = self.del_(key)
        self.insert(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache: self.del_(key)
        self.insert(key, value)
        if len(self.cache)> self.capacity: self.del_(self.head.next.key)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Time: O(n)
# Space: O(n)
