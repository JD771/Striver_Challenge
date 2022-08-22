def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def symm(node1, node2):
            if not node1 or not node2: return node1== node2
            if node1.val != node2.val: return False
            return symm(node1.left, node2.right) and symm(node1.right, node2.left)
        return symm(root.left, root.right)
      
# Time: O(n)
# Space: O(n)
