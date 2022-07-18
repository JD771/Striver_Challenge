class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0
        heights.append(0)
        for i, height in enumerate(heights):
            while heights[stack[-1]]> height:
                h = heights[stack.pop()]
                w = i- stack[-1]-1
                ans = max(ans, h*w)
            stack.append(i)
        heights.pop()
        return ans
      
# Time: O(n)
# Space: O(n)
