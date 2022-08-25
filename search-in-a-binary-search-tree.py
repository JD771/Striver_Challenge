if not root: return
        if root.val == val: return root
        if root.val < val: return self.searchBST(root.right, val)
        else: return self.searchBST(root.left, val)
    
# Time: O(n)
# Space: O(n)
