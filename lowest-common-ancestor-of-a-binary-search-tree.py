def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True: 
            if p.val<root.val and q.val<root.val:
                root = root.left
            elif p.val>root.val and q.val>root.val:
                root =root.right
            else:
                return root
              
# Time: O(n)
# Space: O(n)
