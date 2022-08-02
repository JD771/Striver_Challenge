class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        stack = self.s
        span, cur_price = 1, price
        while stack and stack[-1][1]<= cur_price:
            prev_span, prev_price = stack.pop()
            
            span += prev_span
        stack.append((span, cur_price))
        return span

# Time: O(n)
# Space: O(n)
