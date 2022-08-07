def bottomView(self, root):
        # code here
        queue = deque()
        dic = {}
        if root == None: return list(dic.values())
        queue.append((root, 0))
        while queue:
            q= queue.popleft()
            node = q[0]
            line = q[1]
            
            dic[line] = node.data
            if node.left: queue.append((node.left, line-1))
            if node.right: queue.append((node.right, line+1))
        
        ans = list(sorted(dic.items()))
        a = []
        for i in ans:
            a.append(i[1])
        return a
      
# Time: O(n)
# Space: O(n)
