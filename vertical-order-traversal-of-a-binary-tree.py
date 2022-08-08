from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        def dfs(node,x=0,y=0):
            if not node:return None
            dic[x].append([y,node.val])
            dfs(node.left  ,x-1,y+1)
            dfs(node.right ,x+1,y+1)
        dfs(root)
        return [  [value for _,value in sorted(v)] for k,v  in sorted(dic.items())  ]
      
      
# Time: O(n)
# Space: O(n)
