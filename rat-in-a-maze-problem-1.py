# Backtracking
class Solution:
    def findPath(self, m, n):
        # code here
        def isitsafe(m,n,i,j):
            return 0<=i<n and 0<=j<n and m[i][j]== 1
            
        def recursion(n, i,j, m, ans, path):
            if i== n-1 and j== n-1:
                ans.append(path)
                return
            # (i+1,j) Down, (i,j-1) Left, (i,j+1) Right, (i-1,j) Up
            valid_neighbour = [(1, 0, "D"),(0,-1, "L"),(0, 1, "R"), (-1, 0, "U")]
            for r,c, d in (valid_neighbour):
                if isitsafe(m,n,i+r,j+c):
                    path += d
                    m[i+ r][j+ c] = -1
                    recursion(n, i+r, j+c, m, ans, path)
                    m[i+r][j+c] = 1
                    path = path[:-1]
        i, j = 0,0
        ans = []
        if m[i][j]== 1:
            m[i][j]= -1
            recursion(n,0,0,m, ans,"")
        return ans

# Time: O(n^2)
# Space: O(n^2)
