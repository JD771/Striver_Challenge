# Approach 1: Bit Manipulation (Power set)
nums.sort()
        n = len(nums)
        if n==0: return
        ans = []
        for i in range(1<<n):
            temp = []
            for j in range(n):
                if i & (1<<j):
                    temp.append(nums[j])
            if temp not in ans:
                ans.append(temp)
        return ans
      
# Time: O(2^n log 2^n)
# Space: O(1)

# Approach 2: Recursion
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def recursion(idx,nums, ds, ans):
            ans.append(ds[:])
            for i in range(idx, n):
                if i!= idx and nums[i]== nums[i-1]: continue
                ds.append(nums[i])
                recursion(i+1, nums, ds, ans)
                ds.pop()
        ans = []
        ds = []
        nums.sort()
        recursion(0, nums, ds, ans)
        return ans
      
# Time: O(2^n *n)
# Space: O(2^n *n)
