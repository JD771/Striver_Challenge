# Approach 1: Recursion (Brute Force)
s = ""
        for i in range(1,n+1):
            s+=str(i)
        def P(n,s,idx, ds):
            if idx==n-1:
                ds.append(''.join(s))
                return
            for i in range(idx,n):
                s[i], s[idx] = s[idx], s[i]
                P(n,s, idx+1, ds)
                s[i],s[idx] = s[idx], s[i]
        ds = []
        P(n, list(s), 0, ds)
        ds.sort()
        for i in range(len(ds)):
            if i== k-1:
                return (''.join(ds[i]))
              
# Time: O(n!logn! * n)
# Space: O(n! + k)

# Approach 2: Optimazation
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [i for i in range(1,n+1)]
        ans = ''
        for i in range(1,n+1):
            idx = 0
            fact = math.factorial(n-i)
            
            while fact< k:
                idx+=1
                k-= fact
            ans += str(num[idx])
            del num[idx]
        return ans
      
# Time: O(n^2)
# Space: O(n)
