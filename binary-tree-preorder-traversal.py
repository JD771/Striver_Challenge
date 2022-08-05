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

# Approach 3: Morris Traversal
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Morris Traversal
        res = []
        curr, pre = root, None
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pre= curr.left
                while pre.right and pre.right is not curr: 
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    res.append(curr.val)
                    curr = curr.left
                else:
                    pre.right = None
                    curr = curr.right
        return res

# Time: O(n)
# Space: O(1)
