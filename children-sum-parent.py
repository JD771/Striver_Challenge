def isSumProperty(self, root):
        # code here
        if not root: return 1
        if not root.left and not root.right: return 1
        else:
            summ = 0
            if root.left: summ += root.left.data 
            if root.right: summ += root.right.data
            if not (summ == root.data): return 0
        left = self.isSumProperty(root.left)
        right = self.isSumProperty(root.right)

        return left and right
      
# Time : O(n)
# Space: O(n)/ O(h)
