def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        def dfs(root):
            if not root: return None
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left:
                left.right = root.right
                root.right = root.left
                root.left = None
            last = right or left or root
            return last
        dfs(root)
        
# Time: O(n)
# Space: O(n)
