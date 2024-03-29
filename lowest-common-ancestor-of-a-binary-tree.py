def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root==p or root==q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p,q)
        
        if left and right:
            return root
        if left:
            return left
        else:
            return right
          
# Time: O(n)
# Space: O(n)
