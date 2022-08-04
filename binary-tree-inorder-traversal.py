# Approach 1
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root):
            # Left 
            if root:
                inorder(root.left)
                # base
                ans.append(root.val)
                # Right
                inorder(root.right)
        inorder(root)
        return ans
      
# Time: O(n)
# Space: O(n)
