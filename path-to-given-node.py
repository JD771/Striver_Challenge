def solve(self, A, B):
        ans = []
        def dfs(A, ans, B):
            if not A: return False
            ans.append(A.val)
            if A.val == B: return True
            if dfs(A.left, ans, B) or dfs(A.right, ans, B): return True
            ans.pop()
            return False
        dfs(A,ans, B)
        return ans
      
# Time: O(n)
# Space: O(n)
