def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            while left<right:
                mid = (left + right)//2
                node = TreeNode(nums[mid])
                node.left = dfs(left, mid)
                node.right = dfs(mid+1, right)
                return node
        return dfs(0, len(nums))
      
# Time: O(n)
# Space: O(n)
