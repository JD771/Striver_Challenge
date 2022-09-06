# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: return False
        queue, seen = deque([root]), set()
        while queue:
            cur = queue.popleft()
            if cur.val in seen:
                return True
            else:
                seen.add(k-cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return False

# Time: O(n)
# Space: O(n)
