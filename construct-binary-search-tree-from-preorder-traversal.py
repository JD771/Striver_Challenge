def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    n= len(preorder)
    if n==0: return None
    root = preorder[0]
    for i in range(1, len(preorder)):
      if preorder[i] > root:
          n= i
          break
    left = self.bstFromPreorder(preorder[1:n])
    right = self.bstFromPreorder(preorder[n:])
    return TreeNode(root, left, right)
  
#Time: O(n)
# Space: O(n)
