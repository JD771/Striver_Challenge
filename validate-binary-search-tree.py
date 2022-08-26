def isValidBST(self, root: Optional[TreeNode],lessThan = float('inf'), largerThan = float('-inf')) -> bool:
        if not root: return True
        if not (root.val< lessThan and root.val> largerThan): return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and self.isValidBST(root.right, lessThan, max(largerThan, root.val))

# Time: O(n)
# Space: O(n)
