class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if len(self.s)==0: self.s.append((val,val))
        else: self.s.append((val,min(val, self.s[-1][1])))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]

# Time: O(1) for each function
# Space: O(n)
