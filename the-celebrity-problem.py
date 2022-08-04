def celebrity(self, M, n):
        s = []
        for i in range(n):
            s.append(i)
        
        while len(s)>1:
            a = s.pop()
            b = s.pop()
            
            if M[a][b]== 1: s.append(b)
            else: s.append(a)
        c = s[-1]
        count = 0
        for i in range(n):
            if M[c][i]==0: 
                count+=1
        if count!=n: return -1
        
        count = 0
        for i in range(n):
            if M[i][c]== 1: count+=1
            
        if count!=n-1: return -1
        return c
      
# Time: O(n)
# Space: O(1)
