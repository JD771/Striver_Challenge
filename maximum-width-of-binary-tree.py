class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(0,root)]
        ans = 0
        while q:
            n = len(q)
            nodes = []
            for _ in range(n):
                idx, node = q.pop(0)
                nodes.append(idx)
                if node.left: q.append((2*idx+1, node.left))
                if node.right: q.append((2*idx+2, node.right))
            ans = max(ans, nodes[-1]-nodes[0]+1)
        return ans
      
# Time: O(n)
# Space: O(n)
