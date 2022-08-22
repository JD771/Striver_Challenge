# Recursive

def mirror(self,root):
        # Code here
        if not root: return True
        def mirror(root):
            if not root: return None
            mirror(root.left)
            mirror(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            
        def inorder(node):
            ans = []
            if not node: return None
            inorder(node.left)
            ans.append(node.data)
            inorder(node.right)
        node = mirror(root)
        return inorder(node)
      
# Time: O(n)
# Space: O(h) or O(n)

# Iterative
def mirror(self,root):
        # Code here
        if not root: return True
        q = []
        q.append(root)
        while q:
            node = q.pop(0)
            node.left, node.right = node.right, node.left
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            
        def inorder(node):
            ans = []
            if not node: return None
            inorder(node.left)
            ans.append(node.data)
            inorder(node.right)
        return inorder(root)
      
# Time: O(n)
# Space: O(n)
