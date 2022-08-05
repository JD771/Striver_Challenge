# Approach 1: Recurision

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(root):
            if root:
                ans.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ans
      
# Time: O(n)
# Space: O(n)

# Approach 2: Morris Traversal
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
# Time: O(n)
# Space: O(n)
