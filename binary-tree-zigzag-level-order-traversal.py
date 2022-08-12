# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return None
        q, res = [],[]
        q.append((root,1))
        while q:
            level = []
            for i in range(len(q)):
                node, line = q.pop(0)
                level.append(node.val)
                if node.left: q.append((node.left, line+1))
                if node.right: q.append((node.right, line+1))
            if line%2 == 0: level.reverse()
            res.append(level)
        return res
      
# Time: O(n)
# Space: O(n)
