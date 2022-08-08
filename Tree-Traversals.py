# Inorder, Preorder, postorder in single traversal
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    # Inoreder traversal
    def inorder(root,ans):
        if root== None: return
        inorder(root.left,ans)
        ans.append(root.data)
        inorder(root.right,ans)
        return
    
    # Preporder traversal
    def preorder(root,ans):
        if root== None: return
        ans.append(root.data)
        preorder(root.left,ans)
        preorder(root.right,ans)
        return
    
    # Postorder traversal
    def postorder(root,ans):
        if root==None: return
        postorder(root.left,ans)
        postorder(root.right,ans)
        ans.append(root.data)
        return
    a, b, c = [],[],[]
    inorder(root,a)
    preorder(root,b)
    postorder(root,c)
    return [a,b,c]
  
  # Time: O(n)
  # Space: O(n)
