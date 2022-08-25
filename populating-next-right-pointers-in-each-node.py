def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, nex = root, root.left if root else None
        while cur and nex:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
        
            cur = cur.next
            if not cur:
                cur = nex
                nex = cur.left
        return root
      
# Time: O(n)
# Space: O(1)
