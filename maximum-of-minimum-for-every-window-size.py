from collections import deque
class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        left, right = [-1]* (n+1), [n]*(n+1)
        queue = deque()
        for i, a in enumerate(arr):
            while queue and arr[queue[-1]]>= a:
                queue.pop()
            if queue: left[i] = queue[-1]
            queue.append(i)
            
        while queue: queue.pop()
        for i, a in reversed(list(enumerate(arr))):
            while queue and arr[queue[-1]]>= a:
                queue.pop()
            if queue: right[i] = queue[-1]
            queue.append(i)
        
        ans = [0]* (n+1)
        for i in range(n):
            Len = right[i]- left[i]-1
            ans[Len] = max(ans[Len], arr[i])
        
        for i in range(n-1, 0, -1):
            ans[i] = max(ans[i], ans[i+1])
        ans.remove(ans[0])
        return ans
      
# Time: O(n)
# Space: O(n)
