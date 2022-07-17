from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = defaultdict(int) # key: freq
        self.freq = defaultdict(OrderedDict) # freq(key: val)
        self.min_freq = 0
    
    def move_items(self, key: int, val: int= None)-> int:
        # deletion
        fr = self.items[key]
        v = self.freq[fr].pop(key)
        if val is not None: v = val
        
        # insertion (updated freq & val)
        self.freq[fr+1][key] = v
        self.items[key] +=1
        if self.min_freq == fr and not self.freq[fr]:
            self.min_freq += 1
        return v

    def get(self, key: int) -> int:
        if key not in self.items: return -1
        return self.move_items(key)

    def put(self, key: int, value: int) -> None:
        if not self.capacity: return
        if key in self.items: self.move_items(key, value)
        else:
            if len(self.items) >= self.capacity: self.items.pop(self.freq[self.min_freq].popitem(last = False)[0])
            self.min_freq = 1
            self.items[key] = 1
            self.freq[1][key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Time: O(1) avg
# Space: O(n)
