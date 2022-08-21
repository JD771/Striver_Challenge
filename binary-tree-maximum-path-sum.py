def maxPathSum(self, root: Optional[TreeNode]) -> int:
        summ = float('-inf')
        def dfs(root):
            nonlocal summ
            if not root: return 0
            leftsum = dfs(root.left)
            rightsum = dfs(root.right)
            summ = max(summ,root.val, root.val+ leftsum, root.val + rightsum, root.val + leftsum + rightsum)
            return max(root.val, root.val + max(leftsum, rightsum))
        dfs(root)
        return summ
      
# Time: O(n)
# Space: O(n) or O(h)
