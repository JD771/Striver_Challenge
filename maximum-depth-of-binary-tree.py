def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = 0
        q = []
        q.append((root, 1))
        while q:
            node, level = q.pop(0)
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
        ans = max(level, ans)
        return ans
      
# Time: O(n)
# Space: O(n)
