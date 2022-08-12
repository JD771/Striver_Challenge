def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None: return p==q 
        if p.val!=q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
      
# Time: O(n)
# Space: O(n)
