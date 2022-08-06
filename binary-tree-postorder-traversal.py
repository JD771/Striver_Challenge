# Approach 1: Recursive
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def post(root):
            if root:
                post(root.left)
                post(root.right)
                ans.append(root.val)
        post(root)
        return ans
      
# Time: O(n)
# Space: O(n)

# Approach 2: Morris traversal
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def reverse(left, right):
            while left<right:
                res[left], res[right] = res[right], res[left]
                left+=1
                right-=1
        dummy = TreeNode(None)
        curr = dummy
        curr.left = root
        while curr:
            if curr.left is None:
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right!= curr: pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre = curr.left
                    count = 1
                    while pre and pre.right!= curr: 
                        res.append(pre.val)
                        pre = pre.right
                        count+=1
                    res.append(pre.val)
                    pre.right = None
                    reverse(len(res)-count, len(res)-1)
                    curr = curr.right
        return res
      
# Time: O(n)
# Space: O(1)
