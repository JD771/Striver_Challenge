from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt, days = 0,0
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1: cnt+=1
                if grid[i][j]==2: queue.append([i,j])
        
        dim = [[-1,0],[0,1],[1,0],[0,-1]]
        while queue and cnt>0:
            for q in range(len(queue)):
                i,j = queue.popleft()
                for x,y in dim: 
                    new_x, new_y = x+i, y+j
                    
                    if new_x < 0 or new_x >= n or new_y< 0 or new_y >= m or grid[new_x][new_y]!=1: continue
                    grid[new_x][new_y]=2
                    queue.append([new_x,new_y])
                    cnt-=1
            days +=1
        return days if cnt==0 else -1
        
        
# Time: O(n*m)
# Space: O(n*m)
