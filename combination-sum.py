class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def func(ans, i,target,ds):
            if i==n:
                if target==0:
                    ans.append(ds[:])
                return
            if candidates[i]<=target:
                ds.append(candidates[i])
                func(ans, i, target- candidates[i], ds)
                ds.pop()
            func(ans, i+1, target, ds)
        ans, ds = [], []
        func(ans,0,target, ds)
        return ans
      
# Time: O(2^t * k) # for iterating till target and k recursion depth
# Space: O(k * x) # x is assumed max space taken
