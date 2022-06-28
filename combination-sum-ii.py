# Approach 1: Recursion
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n= len(candidates)
        def func(ans, i, target, ds):
            if i==n:
                if target==0:
                    ans.add(ds)
                return
            if candidates[i]<= target:
                ds.append(candidates[i])
                func(ans, i+1, target-candidates[i], ds)
                ds.pop()
            func(ans, i+1, target, ds)
        ans, ds = set() , []
        candidates.sort()
        func(ans, 0, target, ds)
        return ans
      
# Time: O(2^t * klogn)
# Space: O(k* x)

# Approach 2: Recursion
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n= len(candidates)
        def func(ans, idx, target, ds):
            if idx==n:
                if target==0:
                    ans.append(ds[:])
                return
            for i in range(idx, n):
                if i!= idx and candidates[i]== candidates[i-1]: continue
                if candidates[i]<= target:
                    ds.append(candidates[i])
                    func(ans, i+1, target-candidates[i], ds)
                    ds.pop()
            func(ans, i+1, target, ds)
        ans, ds = [] , []
        candidates.sort()
        func(ans, 0, target, ds)
        return ans
      
# Time: O(2^n)
# Space: O(k)
