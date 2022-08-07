def LeftView(root):
    
    # code here
    ans = []
    # recursive left function
    def rec_left(level, val, ans):
        if val== None: return
        if level== len(ans): ans.append(val.data)
        rec_left(level+1, val.left, ans)
        rec_left(level+1, val.right, ans)
    
    # Call the functions
    rec_left(0, root, ans)
    return ans
  
# Time: O(n) (for traversal till the last level)
# Space: O(h) (hieght of the tree)
