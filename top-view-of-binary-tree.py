def topView(self,root):
        
        # code here
        queue = deque()
        dic = {}
        if root is None: return list(dic.values())
        queue.append((root, 0))
        while queue:
            node, line= queue.popleft()
            dic.setdefault(line, node.data)
            
            
            if node.left: queue.append((node.left, line-1))
            if node.right: queue.append((node.right, line+1))
        a = list(sorted(dic.items()))
        ans = []
        for i in a:
            ans.append(i[1])
        return ans
      
# Time: O(n)
# Space: O(n)
