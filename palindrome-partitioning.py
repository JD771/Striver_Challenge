class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if not s or n==0: return
    
        def func(idx, s, ds, ans):
            if idx==n:
                ans.append(ds[:])
                return
            for i in range(idx,n):
                if palindrome(s,idx, i)== False: continue
                ds.append(s[idx:i+1])
                func(i+1, s, ds, ans)
                ds.pop()
                
        def palindrome(s, start, stop):
            while start<= stop:
                if s[start]!= s[stop]: return False
                start +=1
                stop -=1
            return True
        
        ans = []
        func(0, s, [], ans)
        return ans
      
# Time: O(2^n *k*n/2) #2^n to travel the depth of the recursion tree, k: there are k recursion calls, n/2: for checking if palindrome or not
# Space: O(k*x)
