def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return root
        res, queue = [],[]
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
            res.append(level)
        return res
      
# Time: O(n)
# Space: O(n)
