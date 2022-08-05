# Approach 1: Using Recursion
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


# Approach 2: Using Stack
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s, res = [], []
        curr = root
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            res.append(curr.val)
            curr = curr.right
        return res
    
# Time: O(n)
# Space: O(n)

# Approach 3: Morris Traversal- threaded Binary Tree
 def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        pre = None
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right: pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return res
    
# Time: O(n)
# Space: O(1)
