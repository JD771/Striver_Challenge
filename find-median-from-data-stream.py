class MedianFinder:

    def __init__(self):
        import heapq
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.maxheap,-num)
            temp = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-temp)
        else:
            heapq.heappush(self.minheap,num)
            temp = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -temp)

    def findMedian(self) -> float:
        if len(self.maxheap)==len(self.minheap):
            return (-self.maxheap[0]+ self.minheap[0])/2
        else:
            return self.minheap[0]

# Time: O(1)
# Space: O(n)
